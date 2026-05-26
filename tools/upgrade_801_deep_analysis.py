from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Iterable

import fitz


BASE = Path("801")
TEXT_DIR = BASE / "文本" / "txt"
META_DIR = BASE / "文本" / "metadata"
MANIFEST = BASE / "文本" / "_manifest.json"
ANALYSIS_DIR = BASE / "深度拆解" / "papers"
EVIDENCE_DIR = BASE / "深度拆解" / "extracted_evidence"
TRANSLATION_CACHE = BASE / "深度拆解" / "_translation_cache.json"
PDF_DIR = BASE / "论文"

START_MARKER = "<!-- REAUDIT-2026-05-26 START -->"
END_MARKER = "<!-- REAUDIT-2026-05-26 END -->"

STOP_HEADINGS = [
    "CRediT authorship contribution statement",
    "Declaration of competing interest",
    "Declaration of Competing Interest",
    "Acknowledgements",
    "Acknowledgments",
    "Acknowledgment",
    "Data availability",
    "Appendix",
    "References",
]

STOPWORDS = {
    "the",
    "and",
    "for",
    "that",
    "with",
    "from",
    "this",
    "were",
    "are",
    "was",
    "which",
    "into",
    "using",
    "used",
    "can",
    "has",
    "have",
    "these",
    "such",
    "their",
    "than",
    "then",
    "also",
    "been",
    "under",
    "between",
    "through",
    "based",
    "shown",
    "show",
    "study",
    "results",
    "result",
    "method",
    "methods",
    "model",
    "models",
    "analysis",
    "different",
    "proposed",
    "paper",
    "present",
}

NOUN_HINTS = {
    "tion",
    "sion",
    "ment",
    "ness",
    "ity",
    "ics",
    "ure",
    "ance",
    "ence",
    "ship",
    "ism",
}
ADJ_HINTS = {
    "al",
    "ive",
    "ous",
    "ic",
    "ical",
    "ary",
    "able",
    "ible",
    "less",
    "ant",
    "ent",
}
ACADEMIC_VERBS = [
    "propose",
    "proposed",
    "develop",
    "developed",
    "present",
    "presented",
    "derive",
    "derived",
    "show",
    "shown",
    "demonstrate",
    "demonstrated",
    "reveal",
    "revealed",
    "indicate",
    "indicated",
    "validate",
    "validated",
    "compare",
    "compared",
    "estimate",
    "estimated",
    "predict",
    "predicted",
    "optimize",
    "optimized",
]


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def strip_page_markers(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.startswith("# Source PDF:"):
            continue
        if line.startswith("# Extracted at:"):
            continue
        if line.startswith("# Extraction method:"):
            continue
        if line.startswith("# Pages:"):
            continue
        if line.startswith("# PDF SHA256:"):
            continue
        if re.match(r"^=+ PAGE \d+ / \d+ =+$", line.strip()):
            lines.append("")
            continue
        lines.append(line.rstrip())
    return "\n".join(lines)


def normalize_space(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_section_text(text: str) -> str:
    text = strip_page_markers(text)
    cleaned = []
    for line in text.splitlines():
        raw = line.strip()
        if not raw:
            cleaned.append("")
            continue
        if re.match(r"^[A-Z]\. .+ et al\.\s+.+\(\d{4}\).*$", raw):
            continue
        if re.match(r"^\d{3,5}$", raw):
            continue
        cleaned.append(raw)
    return normalize_space("\n".join(cleaned))


def clean_pdf_block_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def line_key(line: str) -> str:
    line = line.replace("\u00ad", "")
    line = re.sub(r"\s+", " ", line)
    line = line.strip().strip(".:")
    return line.lower()


def heading_variants(title: str) -> list[str]:
    variants = {title}
    variants.add(title.replace(".", ""))
    variants.add(re.sub(r"^(\d+(?:\.\d+)*)\s+", r"\1. ", title))
    variants.add(re.sub(r"^(\d+(?:\.\d+)*)\.\s+", r"\1 ", title))
    variants.add(title.replace("Conclusions", "Conclusion"))
    variants.add(title.replace("Conclusion", "Conclusions"))
    return [line_key(item) for item in variants if item]


def heading_pattern(title: str) -> re.Pattern[str]:
    title = title.strip()
    # Numeric section prefixes often alternate between "3.1" and "3.1." in PDFs.
    m = re.match(r"^(\d+(?:\.\d+)*)(?:\.)?\s+(.+)$", title)
    if m:
        nums = r"\.?\s*".join(re.escape(part) for part in m.group(1).split("."))
        words = re.escape(m.group(2)).replace(r"\ ", r"\s+")
        return re.compile(rf"(?<!\d){nums}\.?\s+{words}\b", flags=re.I)
    words = re.escape(title).replace(r"\ ", r"\s+")
    return re.compile(rf"\b{words}\b", flags=re.I)


def find_heading_span(text: str, title: str, start: int = 0) -> tuple[int, int] | None:
    pattern = heading_pattern(title)
    match = pattern.search(text, pos=start)
    if match:
        return match.span()
    return None


def pdf_blocks(pdf_path: Path) -> list[dict]:
    blocks: list[dict] = []
    doc = fitz.open(pdf_path)
    flags = getattr(fitz, "TEXT_DEHYPHENATE", 0)
    for pageno, page in enumerate(doc):
        width = page.rect.width
        for block in page.get_text("blocks", flags=flags, sort=False):
            x0, y0, x1, y1, text, *_rest = block
            cleaned = clean_pdf_block_text(text)
            if not cleaned:
                continue
            if re.match(r"^\d{1,4}$", cleaned):
                continue
            center = (x0 + x1) / 2
            column = 0 if center < width / 2 else 1
            blocks.append(
                {
                    "page": pageno,
                    "x0": x0,
                    "y0": y0,
                    "x1": x1,
                    "y1": y1,
                    "column": column,
                    "text": cleaned,
                }
            )
    return blocks


def find_pdf_heading_block(blocks: list[dict], title: str) -> tuple[int, re.Match[str]] | None:
    pattern = heading_pattern(title)
    for idx, block in enumerate(blocks):
        match = pattern.search(block["text"])
        if match:
            return idx, match
    return None


def stop_patterns_for(toc: list[dict], toc_index: int) -> list[re.Pattern[str]]:
    item = toc[toc_index]
    current_level = item.get("level", 2)
    patterns = []
    for nxt in toc[toc_index + 1 :]:
        if nxt.get("level", 2) <= current_level:
            patterns.append(heading_pattern(nxt["title"]))
    for stop in STOP_HEADINGS:
        patterns.append(re.compile(rf"\b{re.escape(stop)}\b", flags=re.I))
    return patterns


def trim_at_stop(text: str, patterns: list[re.Pattern[str]]) -> tuple[str, bool]:
    earliest = None
    for pattern in patterns:
        match = pattern.search(text)
        if match and (earliest is None or match.start() < earliest):
            earliest = match.start()
    if earliest is not None:
        return text[:earliest].strip(), True
    return text, False


def extract_pdf_section(pdf_path: Path, toc: list[dict], toc_index: int) -> tuple[str, bool]:
    blocks = pdf_blocks(pdf_path)
    found = find_pdf_heading_block(blocks, toc[toc_index]["title"])
    if found is None:
        return "", False
    heading_idx, heading_match = found
    heading = blocks[heading_idx]
    stop_patterns = stop_patterns_for(toc, toc_index)
    parts: list[str] = []
    after_heading = heading["text"][heading_match.end() :].strip()
    if after_heading:
        trimmed, stopped = trim_at_stop(after_heading, stop_patterns)
        if trimmed:
            parts.append(trimmed)
        if stopped:
            return normalize_space("\n\n".join(parts)), True

    pages = sorted({b["page"] for b in blocks})
    start_page = heading["page"]
    for page in pages:
        if page < start_page:
            continue
        page_blocks = [b for b in blocks if b["page"] == page]
        ordered: list[dict] = []
        if page == start_page:
            if heading["column"] == 0:
                ordered.extend(
                    sorted(
                        [b for b in page_blocks if b["column"] == 0 and b["y0"] > heading["y1"] - 2],
                        key=lambda b: (b["y0"], b["x0"]),
                    )
                )
                ordered.extend(
                    sorted(
                        [b for b in page_blocks if b["column"] == 1],
                        key=lambda b: (b["y0"], b["x0"]),
                    )
                )
            else:
                ordered.extend(
                    sorted(
                        [b for b in page_blocks if b["column"] == heading["column"] and b["y0"] > heading["y1"] - 2],
                        key=lambda b: (b["y0"], b["x0"]),
                    )
                )
        else:
            ordered.extend(sorted([b for b in page_blocks if b["column"] == 0], key=lambda b: (b["y0"], b["x0"])))
            ordered.extend(sorted([b for b in page_blocks if b["column"] == 1], key=lambda b: (b["y0"], b["x0"])))
        for block in ordered:
            if re.match(r"^(Fig\.|Figure|Table)\s+\d+", block["text"], flags=re.I):
                continue
            trimmed, stopped = trim_at_stop(block["text"], stop_patterns)
            if trimmed:
                parts.append(trimmed)
            if stopped:
                return normalize_space("\n\n".join(parts)), True
    return normalize_space("\n\n".join(parts)), True


def extract_pdf_abstract(pdf_path: Path) -> tuple[str, bool]:
    blocks = pdf_blocks(pdf_path)
    found = None
    for idx, block in enumerate(blocks):
        if re.search(r"A\s+B\s+S\s+T\s+R\s+A\s+C\s+T", block["text"], flags=re.I):
            found = idx, block
            break
    if found is None:
        return "", False
    idx, heading = found
    intro_pat = re.compile(r"\b1\.?\s+Introduction\b", flags=re.I)
    intro_y = None
    for block in blocks:
        if block["page"] == heading["page"] and intro_pat.search(block["text"]):
            intro_y = block["y0"]
            break
    parts = []
    for block in sorted([b for b in blocks if b["page"] == heading["page"]], key=lambda b: (b["y0"], b["x0"])):
        if block["y0"] <= heading["y1"] - 2:
            continue
        if intro_y is not None and block["y0"] >= intro_y - 2:
            break
        if block["x0"] < heading["x0"] - 10:
            continue
        trimmed, stopped = trim_at_stop(block["text"], [intro_pat])
        if trimmed and not trimmed.lower().startswith("keywords"):
            parts.append(trimmed)
        if stopped:
            break
    abstract = normalize_space("\n\n".join(parts))
    return abstract, bool(abstract)


def extract_pdf_references(pdf_path: Path) -> tuple[str, list[str]]:
    blocks = pdf_blocks(pdf_path)
    found = None
    for idx, block in enumerate(blocks):
        if re.fullmatch(r"References", block["text"].strip(), flags=re.I) or re.search(r"\bReferences\b", block["text"], flags=re.I):
            found = idx, block
    if found is None:
        return "", []
    idx, heading = found
    parts = []
    pages = sorted({b["page"] for b in blocks})
    for page in pages:
        if page < heading["page"]:
            continue
        page_blocks = [b for b in blocks if b["page"] == page]
        if page == heading["page"]:
            left = [b for b in page_blocks if b["column"] == 0 and b["y0"] > heading["y1"] - 2]
            right = [b for b in page_blocks if b["column"] == 1]
            ordered = sorted(left, key=lambda b: (b["y0"], b["x0"])) + sorted(right, key=lambda b: (b["y0"], b["x0"]))
        else:
            ordered = sorted([b for b in page_blocks if b["column"] == 0], key=lambda b: (b["y0"], b["x0"]))
            ordered += sorted([b for b in page_blocks if b["column"] == 1], key=lambda b: (b["y0"], b["x0"]))
        for block in ordered:
            parts.append(block["text"])
    block = normalize_space("\n".join(parts))
    entries = parse_reference_entries(block)
    return block, entries


def is_reference_start(line: str) -> bool:
    if re.match(r"^\[\d+\]", line) or re.match(r"^\d+\.\s", line):
        return True
    # Author-year styles, e.g. "Akgün, M.A., Garcelon, J.H., 2001."
    if re.match(r"^[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+,\s+.+\b(?:19|20)\d{2}[a-z]?\.", line):
        return True
    return False


def parse_reference_entries(block: str) -> list[str]:
    entries: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if is_reference_start(stripped):
            if current:
                entries.append(normalize_space(" ".join(current)))
            current = [stripped]
        elif current:
            current.append(stripped)
    if current:
        entries.append(normalize_space(" ".join(current)))
    if len(entries) < 10:
        chunks = re.split(r"(?=\[\d+\]|\b\d+\.\s+[A-Z])", block)
        chunk_entries = [normalize_space(c) for c in chunks if is_reference_start(c.strip())]
        if len(chunk_entries) > len(entries):
            entries = chunk_entries
    return entries


def find_heading_line(lines: list[str], title: str, start: int = 0) -> int | None:
    keys = set(heading_variants(title))
    for idx in range(start, len(lines)):
        if line_key(lines[idx]) in keys:
            return idx
    return None


def extract_by_toc(text: str, toc: list[dict], toc_index: int) -> tuple[str, bool]:
    clean = strip_page_markers(text)
    lines = clean.splitlines()
    item = toc[toc_index]
    start_idx = find_heading_line(lines, item["title"])
    if start_idx is None:
        start_span = find_heading_span(clean, item["title"])
        if start_span is None:
            return "", False
        end_pos = None
        current_level = item.get("level", 2)
        for nxt in toc[toc_index + 1 :]:
            if nxt.get("level", 2) <= current_level:
                next_span = find_heading_span(clean, nxt["title"], start_span[1])
                if next_span is not None:
                    end_pos = next_span[0]
                    break
        if end_pos is None:
            stop_matches = []
            for stop in STOP_HEADINGS:
                sm = re.search(rf"\b{re.escape(stop)}\b", clean[start_span[1] :], flags=re.I)
                if sm:
                    stop_matches.append(start_span[1] + sm.start())
            end_pos = min(stop_matches) if stop_matches else len(clean)
        return clean_section_text(clean[start_span[0] : end_pos]), True

    end_idx = None
    current_level = item.get("level", 2)
    for nxt in toc[toc_index + 1 :]:
        if nxt.get("level", 2) <= current_level:
            candidate = find_heading_line(lines, nxt["title"], start_idx + 1)
            if candidate is not None:
                end_idx = candidate
                break
    if end_idx is None:
        for idx in range(start_idx + 1, len(lines)):
            key = line_key(lines[idx])
            if any(key.startswith(line_key(stop).lower()) for stop in STOP_HEADINGS):
                end_idx = idx
                break
    if end_idx is None:
        end_idx = len(lines)
    return clean_section_text("\n".join(lines[start_idx:end_idx])), True


def first_main_heading(toc: list[dict]) -> str | None:
    for item in toc:
        title = item.get("title", "")
        if item.get("level", 2) >= 2 and re.match(r"^1\.?\s+", title):
            return title
    return None


def infer_toc_from_text(text: str) -> list[dict]:
    toc: list[dict] = []
    current_page = 1
    seen: set[str] = set()
    for line in text.splitlines():
        pm = re.match(r"^=+ PAGE (\d+) / \d+ =+$", line.strip())
        if pm:
            current_page = int(pm.group(1))
            continue
        clean = line.strip()
        if not clean:
            continue
        for match in re.finditer(
            r"(?:(?<=^)|(?<=\s{2}))(\d+(?:\.\d+)*(?:\.)?\s+[A-Z][A-Za-z][A-Za-z0-9,\-–—:/() ]{2,90})",
            clean,
        ):
            title = normalize_space(match.group(1)).rstrip(".")
            if len(title.split()) > 14:
                continue
            num = re.match(r"^(\d+(?:\.\d+)*)", title)
            level = 2 + (num.group(1).count(".") if num else 0)
            key = line_key(title)
            if key not in seen:
                toc.append({"level": level, "title": title, "page": current_page})
                seen.add(key)
        for stop in ["References", "Acknowledgements", "Acknowledgments", "Declaration of competing interest"]:
            if re.search(rf"\b{re.escape(stop)}\b", clean):
                key = line_key(stop)
                if key not in seen:
                    toc.append({"level": 2, "title": stop, "page": current_page})
                    seen.add(key)
    toc.sort(key=lambda item: (item.get("page", 0), len(item.get("title", ""))))
    # Restore likely numeric order, with non-number back matter at the end of each page.
    def order_key(item: dict) -> tuple:
        m = re.match(r"^(\d+(?:\.\d+)*)", item["title"])
        if m:
            return tuple(int(part) for part in m.group(1).split(".")) + (0,)
        return (999, item.get("page", 0), item["title"])

    return sorted(toc, key=order_key)


def remove_keyword_left_column(block: str, keywords: str | None) -> str:
    known = []
    if keywords:
        known = [line_key(k.strip().strip('"')) for k in keywords.split(",") if k.strip()]
    output: list[str] = []
    for line in block.splitlines():
        raw = line.rstrip()
        if not raw.strip():
            output.append("")
            continue
        if "Keywords:" in raw:
            parts = re.split(r"\s{2,}", raw, maxsplit=1)
            if len(parts) == 2 and parts[1].strip():
                output.append(parts[1].strip())
            continue
        key = line_key(raw)
        if known and any(key == k or key.startswith(k + " ") for k in known):
            parts = re.split(r"\s{2,}", raw, maxsplit=1)
            if len(parts) == 2 and len(parts[1].strip()) > 30:
                output.append(parts[1].strip())
            continue
        if len(raw) - len(raw.lstrip()) > 25:
            output.append(raw.strip())
        else:
            output.append(raw.strip())
    text = "\n".join(output)
    text = re.sub(r"\bA R T I C L E I N F O\b", "", text)
    text = re.sub(r"\bA B S T R A C T\b", "", text)
    text = re.sub(r"\n\s*[A-Z][\w\- ]+(?:\n|$)", lambda m: m.group(0), text)
    return normalize_space(text)


def extract_abstract(text: str, toc: list[dict], keywords: str | None) -> tuple[str, bool]:
    clean = strip_page_markers(text)
    match = re.search(r"A\s+B\s+S\s+T\s+R\s+A\s+C\s+T", clean, flags=re.I)
    if not match:
        match = re.search(r"\bAbstract\b", clean, flags=re.I)
    if not match:
        return "", False
    start = match.end()
    stop_title = first_main_heading(toc)
    stop = None
    if stop_title:
        lines = clean.splitlines()
        start_line = clean[:start].count("\n")
        stop_line = find_heading_line(lines, stop_title, start_line)
        if stop_line is not None:
            stop = sum(len(line) + 1 for line in lines[:stop_line])
    if stop is None:
        intro = re.search(r"\n\s*1\.?\s+Introduction\b", clean[start:], flags=re.I)
        stop = start + intro.start() if intro else start + 5000
    block = clean[start:stop]
    abstract = remove_keyword_left_column(block, keywords)
    abstract = re.sub(r"\s*\* Correspond.*$", "", abstract, flags=re.S)
    return abstract.strip(), bool(abstract.strip())


def find_conclusion(toc: list[dict], text: str) -> tuple[str, str, bool]:
    candidates = [
        i
        for i, item in enumerate(toc)
        if re.search(r"\bconclusions?\b|\bconcluding remarks\b", item.get("title", ""), flags=re.I)
    ]
    for idx in candidates:
        section, ok = extract_by_toc(text, toc, idx)
        if ok and len(section) > 80:
            return toc[idx]["title"], section, True

    discussion_candidates = [
        i
        for i, item in enumerate(toc)
        if re.search(r"\bdiscussion\b", item.get("title", ""), flags=re.I)
    ]
    for idx in reversed(discussion_candidates):
        section, ok = extract_by_toc(text, toc, idx)
        if ok and len(section) > 80:
            paras = [p.strip() for p in re.split(r"\n\s*\n", section) if p.strip()]
            tail = "\n\n".join(paras[-2:]) if len(paras) >= 2 else section
            return toc[idx]["title"] + "（无独立 Conclusion，取末段）", tail, False
    return "未识别", "", False


def extract_references(text: str) -> tuple[str, list[str]]:
    clean = strip_page_markers(text)
    matches = list(re.finditer(r"\n\s*References\b", clean, flags=re.I))
    m = matches[-1] if matches else None
    if not m:
        return "", []
    block = clean[m.end() :]
    block = re.split(r"\n\s*(Appendix|Supplementary)\b", block, maxsplit=1)[0]
    block = clean_section_text(block)
    entries = parse_reference_entries(block)
    if not entries and block:
        chunks = re.split(r"(?=\[\d+\])", block)
        entries = [normalize_space(c) for c in chunks if len(c.strip()) > 20]
    if block:
        chunks = re.split(r"(?=\[\d+\])", block)
        chunk_entries = [normalize_space(c) for c in chunks if re.match(r"^\[\d+\]", c.strip())]
        if len(chunk_entries) > len(entries):
            entries = chunk_entries
    return block, entries


def tokenize(text: str) -> list[str]:
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text) if w.lower() not in STOPWORDS]


def sentence_split(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
    return [p.strip() for p in parts if len(p.strip()) > 35]


def pick_sentences(sentences: list[str], keywords: Iterable[str], limit: int = 3) -> list[str]:
    out = []
    kws = [k.lower() for k in keywords]
    for sentence in sentences:
        lower = sentence.lower()
        if any(k in lower for k in kws):
            out.append(sentence)
        if len(out) >= limit:
            break
    return out


def make_template(sentence: str) -> str:
    tpl = sentence
    tpl = re.sub(r"\b\d+(?:\.\d+)?\s*%?", "X", tpl)
    tpl = re.sub(r"\b[A-Z]{2,}(?:-[A-Z]{2,})?\b", "METHOD", tpl)
    tpl = re.sub(r"\bheat flux distribution\b", "X", tpl, flags=re.I)
    tpl = re.sub(r"\bhypersonic flight vehicles?\b", "Y", tpl, flags=re.I)
    return tpl


def count_citations(text: str) -> tuple[int, list[str]]:
    clusters = re.findall(r"\[(?:\d+(?:\s*[-,]\s*\d+)*\s*)+\]", text)
    return len(clusters), clusters


def classify_heading(title: str) -> str:
    lower = title.lower()
    if "introduction" in lower:
        return "背景/领域定位"
    if "method" in lower or "model" in lower or "framework" in lower or "formulation" in lower:
        return "方法/模型"
    if "result" in lower or "discussion" in lower or "validation" in lower or "case" in lower:
        return "结果/讨论/验证"
    if "conclusion" in lower:
        return "结论"
    if "appendix" in lower:
        return "附录"
    if "reference" in lower:
        return "参考文献"
    return "对象/问题/模块"


def translation_cache() -> dict[str, str]:
    if TRANSLATION_CACHE.exists():
        return json.loads(TRANSLATION_CACHE.read_text(encoding="utf-8"))
    return {}


def save_translation_cache(cache: dict[str, str]) -> None:
    TRANSLATION_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def split_for_translation(text: str, max_chars: int = 900) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 > max_chars and current:
            chunks.append(current.strip())
            current = sentence
        else:
            current += (" " if current else "") + sentence
    if current.strip():
        chunks.append(current.strip())
    return chunks


def translate_google(text: str, cache: dict[str, str], key: str, enabled: bool) -> str:
    if not text.strip():
        return ""
    if key in cache:
        return cache[key]
    if not enabled:
        return "（未启用自动翻译；保留原文用于复核。）"
    translated_parts: list[str] = []
    for idx, chunk in enumerate(split_for_translation(text), start=1):
        ckey = f"{key}::chunk::{idx}"
        if ckey in cache:
            translated_parts.append(cache[ckey])
            continue
        params = urllib.parse.urlencode(
            {
                "client": "gtx",
                "sl": "en",
                "tl": "zh-CN",
                "dt": "t",
                "q": chunk,
            }
        )
        url = "https://translate.googleapis.com/translate_a/single"
        try:
            request = urllib.request.Request(
                url,
                data=params.encode("utf-8"),
                headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=25) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            translated = "".join(part[0] for part in data[0] if part and part[0])
            cache[ckey] = translated
            translated_parts.append(translated)
            time.sleep(0.2)
        except Exception as exc:  # noqa: BLE001
            translated_parts.append(f"（自动翻译失败：{exc}）")
            break
    result = "\n\n".join(translated_parts).strip()
    if "自动翻译失败" not in result:
        cache[key] = result
    return result


def stats_for(text: str, section_texts: dict[str, str]) -> dict:
    words = tokenize(text)
    word_counter = Counter(words)
    nouns = Counter(w for w in words if any(w.endswith(suf) for suf in NOUN_HINTS))
    adjs = Counter(w for w in words if any(w.endswith(suf) for suf in ADJ_HINTS))
    advs = Counter(w for w in words if w.endswith("ly"))
    verbs = Counter(w for w in words if w in ACADEMIC_VERBS or w.rstrip("ed") in ACADEMIC_VERBS)
    passive = len(re.findall(r"\b(?:is|are|was|were|be|been|being)\s+\w+ed\b", text, flags=re.I))
    we_active = len(re.findall(r"\bwe\s+(?:propose|develop|present|show|demonstrate|derive|use|construct|introduce)\b", text, flags=re.I))
    present = len(re.findall(r"\b(?:is|are|shows?|indicates?|suggests?|demonstrates?|provides?|enables?)\b", text, flags=re.I))
    past = len(re.findall(r"\b(?:was|were|\w+ed)\b", text, flags=re.I))
    perfect = len(re.findall(r"\b(?:has|have)\s+\w+ed\b", text, flags=re.I))
    modal = len(re.findall(r"\b(?:may|might|can|could|should|would)\b", text, flags=re.I))
    ngrams2 = Counter(zip(words, words[1:]))
    ngrams3 = Counter(zip(words, words[1:], words[2:]))
    section_freq = {
        name: Counter(tokenize(value)).most_common(8)
        for name, value in section_texts.items()
        if value
    }
    return {
        "top_words": word_counter.most_common(20),
        "top_nouns": nouns.most_common(15),
        "top_verbs": verbs.most_common(15),
        "top_adjs": adjs.most_common(15),
        "top_advs": advs.most_common(15),
        "top_bigrams": [(" ".join(k), v) for k, v in ngrams2.most_common(12)],
        "top_trigrams": [(" ".join(k), v) for k, v in ngrams3.most_common(12)],
        "passive_estimate": passive,
        "we_active_estimate": we_active,
        "present_estimate": present,
        "past_estimate": past,
        "perfect_estimate": perfect,
        "modal_estimate": modal,
        "section_freq": section_freq,
    }


def citation_analysis(full_text: str, intro_text: str, references: list[str], journal_hint: str) -> dict:
    total_count, clusters = count_citations(full_text)
    intro_count, intro_clusters = count_citations(intro_text)
    years: list[int] = []
    journals: Counter[str] = Counter()
    for ref in references:
        for year in re.findall(r"\b(19\d{2}|20\d{2})\b", ref):
            years.append(int(year))
        for journal in [
            "Aerospace Science and Technology",
            "Applied Thermal Engineering",
            "Composite Structures",
            "International Journal of Heat and Mass Transfer",
            "Acta Astronautica",
            "Chinese Journal of Aeronautics",
            "Probabilistic Engineering Mechanics",
            "Journal of Fluids and Structures",
            "Journal of Alloys and Compounds",
        ]:
            if journal.lower() in ref.lower():
                journals[journal] += 1
    recent = len([y for y in years if y >= 2021])
    classic = len([y for y in years if y < 2010])
    same_journal = journals[journal_hint] if journal_hint else 0
    gap_lines = []
    for sentence in sentence_split(intro_text):
        lower = sentence.lower()
        if any(k in lower for k in ["however", "limited", "lack", "few", "remain", "challenge", "not", "still"]):
            if re.search(r"\[\d+", sentence):
                gap_lines.append(sentence)
            if len(gap_lines) >= 4:
                break
    return {
        "in_text_citation_clusters": total_count,
        "intro_citation_clusters": intro_count,
        "sample_clusters": clusters[:12],
        "intro_sample_clusters": intro_clusters[:12],
        "reference_count": len(references),
        "reference_year_count": len(years),
        "recent_2021_plus": recent,
        "classic_pre_2010": classic,
        "same_journal_refs": same_journal,
        "top_journals": journals.most_common(6),
        "gap_citation_sentences": gap_lines,
    }


def format_pairs(pairs: list[tuple[str, int]]) -> str:
    return "；".join(f"{word}({count})" for word, count in pairs) if pairs else "未识别"


def block_quote(text: str) -> str:
    if not text.strip():
        return "> 未识别。"
    return "\n".join("> " + line for line in text.strip().splitlines())


def local_evidence_note(stem: str, field: str) -> str:
    label = "摘要" if field == "abstract" else "结论"
    return block_quote(
        "公开库不直接展示完整英文"
        + label
        + "原文；完整摘录保存在本地忽略目录 "
        + f"`801/深度拆解/extracted_evidence/{stem}.json` 的 `{field}` 字段，"
        + f"以及 `801/深度拆解/local_full_reports/{stem}.md`。"
        + "本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。"
    )


def infer_logic(abstract: str, intro: str, conclusion: str) -> dict[str, str]:
    combined = " ".join([abstract, intro[:2500], conclusion])
    sentences = sentence_split(combined)
    problem = pick_sentences(sentences, ["challenging", "important", "essential", "need", "demand", "requires"], 3)
    gap = pick_sentences(sentences, ["however", "limited", "lack", "remain", "not been", "few", "difficult"], 3)
    method = pick_sentences(sentences, ["propose", "develop", "present", "method", "model", "framework", "approach"], 3)
    increment = pick_sentences(sentences, ["achieve", "improve", "provide", "enable", "reveal", "demonstrate", "outperform"], 3)
    return {
        "problem": " ".join(problem) if problem else "需结合 Introduction 首段复核。",
        "gap": " ".join(gap) if gap else "需结合 Introduction 的文献转折句复核。",
        "method": " ".join(method) if method else "需结合 Method/Framework 章节复核。",
        "increment": " ".join(increment) if increment else "需结合 Results/Conclusion 的量化结果复核。",
    }


def build_reaudit_block(record: dict, meta: dict, text: str, translate: bool, cache: dict[str, str]) -> tuple[str, dict]:
    toc = meta.get("toc") or record.get("toc") or []
    if not toc:
        toc = infer_toc_from_text(text)
    title = meta.get("title") or record.get("title") or record["stem"]
    pdf_path = PDF_DIR / record.get("pdf_name", f"{record['stem']}.pdf")
    if pdf_path.exists():
        abstract, abstract_ok = extract_pdf_abstract(pdf_path)
        if not abstract_ok or len(abstract) < 80:
            abstract, abstract_ok = extract_abstract(text, toc, meta.get("keywords") or record.get("keywords"))
    else:
        abstract, abstract_ok = extract_abstract(text, toc, meta.get("keywords") or record.get("keywords"))

    conclusion_heading, conclusion, conclusion_ok = find_conclusion(toc, text)
    if pdf_path.exists():
        candidates = [
            i
            for i, item in enumerate(toc)
            if re.search(r"\bconclusions?\b|\bconcluding remarks\b", item.get("title", ""), flags=re.I)
        ]
        for idx in candidates:
            pdf_conclusion, pdf_ok = extract_pdf_section(pdf_path, toc, idx)
            if pdf_ok and len(pdf_conclusion) > 80:
                conclusion_heading = toc[idx]["title"]
                conclusion = pdf_conclusion
                conclusion_ok = True
                break
        if not conclusion_ok:
            discussion_candidates = [
                i
                for i, item in enumerate(toc)
                if re.search(r"\bdiscussion\b", item.get("title", ""), flags=re.I)
            ]
            for idx in reversed(discussion_candidates):
                pdf_discussion, pdf_ok = extract_pdf_section(pdf_path, toc, idx)
                if pdf_ok and len(pdf_discussion) > 80:
                    paras = [p.strip() for p in re.split(r"\n\s*\n", pdf_discussion) if p.strip()]
                    conclusion_heading = toc[idx]["title"] + "（无独立 Conclusion，取末段）"
                    conclusion = "\n\n".join(paras[-2:]) if len(paras) >= 2 else pdf_discussion
                    break

    if pdf_path.exists():
        references_block, references = extract_pdf_references(pdf_path)
        if not references:
            references_block, references = extract_references(text)
    else:
        references_block, references = extract_references(text)

    intro = ""
    intro_idx = next((i for i, item in enumerate(toc) if re.search(r"\bIntroduction\b", item.get("title", ""), flags=re.I)), None)
    if intro_idx is not None:
        if pdf_path.exists():
            intro, _ = extract_pdf_section(pdf_path, toc, intro_idx)
        else:
            intro, _ = extract_by_toc(text, toc, intro_idx)

    section_texts = {
        "Abstract": abstract,
        "Introduction": intro,
        "Conclusion": conclusion,
    }
    stats = stats_for(text[: max(0, text.lower().find("references"))] if "References" in text else text, section_texts)
    subject = meta.get("subject") or record.get("subject") or ""
    journal_hint = subject.split(",")[0].strip() if "," in subject else ""
    cites = citation_analysis(text, intro, references, journal_hint)
    logic = infer_logic(abstract, intro, conclusion)
    sentences = sentence_split(" ".join([abstract, intro, conclusion]))
    sentence_groups = {
        "背景句": pick_sentences(sentences, ["important", "essential", "critical", "plays", "requires"], 3),
        "Gap句": pick_sentences(sentences, ["however", "limited", "lack", "remain", "challenge", "difficult"], 3),
        "方法句": pick_sentences(sentences, ["propose", "develop", "present", "method", "model", "framework"], 3),
        "结果句": pick_sentences(sentences, ["results", "show", "demonstrate", "achieve", "indicate"], 3),
        "贡献句": pick_sentences(sentences, ["provide", "enable", "reveal", "establish", "contribute"], 3),
        "限制/边界句": pick_sentences(sentences, ["may", "could", "limited", "only", "future", "should"], 3),
    }

    abstract_zh = translate_google(abstract, cache, f"{record['stem']}::abstract", translate)
    conclusion_zh = translate_google(conclusion, cache, f"{record['stem']}::conclusion", translate)

    headings = []
    for item in toc:
        level = int(item.get("level", 2))
        if level == 1:
            continue
        indent = "  " * max(0, level - 2)
        headings.append(
            f"{indent}- L{level} p.{item.get('page', '?')}: {item.get('title', '').strip()} "
            f"（{classify_heading(item.get('title', ''))}）"
        )
    heading_table = [
        "| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for item in toc:
        if int(item.get("level", 2)) == 1:
            continue
        t = item.get("title", "").strip().replace("|", "\\|")
        heading_table.append(
            f"| {t} | {item.get('page', '?')} | {item.get('level', '?')} | {classify_heading(t)} | "
            "来自 metadata TOC，正式分析按此章节点名复核 |"
        )

    sentence_lines = []
    for group, examples in sentence_groups.items():
        sentence_lines.append(f"#### {group}")
        if not examples:
            sentence_lines.append("- 未在抽取文本中稳定识别，需人工从对应章节补充。")
        for s in examples[:3]:
            sentence_lines.append(f"- 原句/结构：{s}")
            sentence_lines.append(f"  可迁移模板：{make_template(s)}")

    ref_sample = references[:12]
    ref_lines = [f"- {ref}" for ref in ref_sample] if ref_sample else ["- 未解析出结构化参考文献条目。"]
    gap_lines = [f"- {s}" for s in cites["gap_citation_sentences"]] or ["- 未在 Introduction 中自动识别到带引用的 gap 句；需人工复核文献转折段。"]

    block = f"""{START_MARKER}

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/{record['stem']}.txt` 与 `801/文本/metadata/{record['stem']}.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

{chr(10).join(headings) if headings else "- 未从 metadata 中识别到 TOC。"}

### 20.2 章节名功能分析

{chr(10).join(heading_table)}

### 20.3 摘要完整摘录（本地证据）

抽取状态：{"成功" if abstract_ok else "未识别"}

{local_evidence_note(record['stem'], 'abstract')}

### 20.4 摘要中文翻译

{block_quote(abstract_zh)}

### 20.5 结论完整摘录（本地证据）

结论章节识别：{conclusion_heading}；状态：{"独立结论章节" if conclusion_ok else "无独立 Conclusion 或使用替代总结段"}

{local_evidence_note(record['stem'], 'conclusion')}

### 20.6 结论中文翻译

{block_quote(conclusion_zh)}

### 20.7 论文逻辑脉络复核

- 提出的问题：{logic['problem']}
- 旧方法/已有研究不足：{logic['gap']}
- 本文解决方式：{logic['method']}
- 学术/工程增量：{logic['increment']}
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：{cites['in_text_citation_clusters']}
- Introduction 引用簇数量（估计）：{cites['intro_citation_clusters']}
- References 条目数（解析）：{cites['reference_count']}
- 可识别年份条目数：{cites['reference_year_count']}
- 近五年/近年文献（2021+）数量：{cites['recent_2021_plus']}
- 经典文献（2010年前）数量：{cites['classic_pre_2010']}
- 同刊引用数量（按 subject 粗略匹配）：{cites['same_journal_refs']}
- 高频来源期刊（粗略）：{format_pairs(cites['top_journals'])}
- 引用簇样例：{", ".join(cites['sample_clusters'][:12]) if cites['sample_clusters'] else "未识别"}

带引用的 gap/转折句样例：

{chr(10).join(gap_lines)}

References 解析样例（前12条）：

{chr(10).join(ref_lines)}

### 20.9 常用词、词类、语态与时态

- 高频词：{format_pairs(stats['top_words'])}
- 高频名词化/学术名词：{format_pairs(stats['top_nouns'])}
- 高频学术动词：{format_pairs(stats['top_verbs'])}
- 高频形容词：{format_pairs(stats['top_adjs'])}
- 高频副词：{format_pairs(stats['top_advs'])}
- 高频二词短语：{format_pairs(stats['top_bigrams'])}
- 高频三词短语：{format_pairs(stats['top_trigrams'])}
- 被动语态估计：{stats['passive_estimate']}；`we + 动作动词` 主动句估计：{stats['we_active_estimate']}
- 一般现在时线索：{stats['present_estimate']}；一般过去时线索：{stats['past_estimate']}；现在完成时线索：{stats['perfect_estimate']}；情态动词线索：{stats['modal_estimate']}

章节词频：

{chr(10).join(f"- {sec}: {format_pairs(freqs)}" for sec, freqs in stats['section_freq'].items())}

### 20.10 句型库扩充（每类多句）

{chr(10).join(sentence_lines)}

### 20.11 抽取失败与人工复核提示

- 摘要抽取：{"正常" if abstract_ok else "失败，需要从 PDF 首页人工复核"}
- 结论抽取：{"正常" if conclusion else "失败，需要人工定位 Conclusion/Discussion 末段"}
- 引文解析：{"正常" if references else "References 未结构化解析，需检查是否为非数字编号或抽取串栏"}
- 章节树：{"正常" if toc else "metadata 未提供 TOC，需要从 PDF 版面人工补录"}
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

{END_MARKER}
"""
    evidence = {
        "stem": record["stem"],
        "title": title,
        "abstract_ok": abstract_ok,
        "abstract": abstract,
        "abstract_zh": abstract_zh,
        "conclusion_heading": conclusion_heading,
        "conclusion_ok": conclusion_ok,
        "conclusion": conclusion,
        "conclusion_zh": conclusion_zh,
        "toc": toc,
        "reference_count": len(references),
        "citation_analysis": cites,
        "logic": logic,
        "stats": stats,
    }
    return block, evidence


def replace_block(original: str, block: str) -> str:
    original = original.replace("jmps/文本/txt/", "801/文本/txt/")
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), flags=re.S)
    if pattern.search(original):
        return pattern.sub(block.strip(), original)
    return original.rstrip() + "\n\n" + block.strip() + "\n"


def main() -> None:
    from integrate_801_reaudit_into_reports import main as integrated_main

    integrated_main()
    return

    parser = argparse.ArgumentParser(description="Upgrade 801 deep analysis reports with strict extracted evidence.")
    parser.add_argument("--translate", action="store_true", help="Use public Google Translate endpoint for abstract/conclusion draft translations.")
    parser.add_argument("--limit", type=int, default=0, help="Process only the first N papers for smoke testing.")
    args = parser.parse_args()

    manifest = read_json(MANIFEST)
    cache = translation_cache()
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    processed = 0
    failures: list[str] = []
    for record in manifest[: args.limit or None]:
        stem = record["stem"]
        txt_path = TEXT_DIR / f"{stem}.txt"
        meta_path = META_DIR / f"{stem}.json"
        report_path = ANALYSIS_DIR / f"{stem}.md"
        if not txt_path.exists() or not meta_path.exists() or not report_path.exists():
            failures.append(f"{stem}: missing input/report")
            continue
        text = txt_path.read_text(encoding="utf-8", errors="replace")
        meta = read_json(meta_path)
        block, evidence = build_reaudit_block(record, meta, text, args.translate, cache)
        report = report_path.read_text(encoding="utf-8", errors="replace")
        report_path.write_text(replace_block(report, block), encoding="utf-8")
        (EVIDENCE_DIR / f"{stem}.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
        processed += 1
        save_translation_cache(cache)
        print(f"[{processed}/{len(manifest[: args.limit or None])}] {stem}", flush=True)

    save_translation_cache(cache)
    print(f"processed={processed} failures={len(failures)} translate={args.translate}")
    if failures:
        print("\n".join(failures))


if __name__ == "__main__":
    main()
