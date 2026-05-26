from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable


sys.path.insert(0, str(Path(__file__).resolve().parent))
import upgrade_801_deep_analysis as legacy  # noqa: E402


BASE = Path("801")
TEXT_DIR = BASE / "文本" / "txt"
META_DIR = BASE / "文本" / "metadata"
MANIFEST = BASE / "文本" / "_manifest.json"
REPORT_DIR = BASE / "深度拆解" / "papers"
EVIDENCE_DIR = BASE / "深度拆解" / "extracted_evidence"
TRANSLATION_CACHE = BASE / "深度拆解" / "_translation_cache.json"
PDF_DIR = BASE / "论文"

LEGACY_REAUDIT_START = "<!-- REAUDIT-2026-05-26 START -->"
LEGACY_REAUDIT_END = "<!-- REAUDIT-2026-05-26 END -->"
INTEGRATED_PREFIX = "REAUDIT-INTEGRATED-2026-05-26"

TARGET_HEADINGS = {
    "STATUS": "## 0. 读取说明",
    "ABSTRACT": "## 2. 摘要与核心信息提取",
    "LOGIC": "## 7. 论证链条复原",
    "STRUCTURE": "## 11. 章节结构与篇章布局",
    "LANGUAGE": "## 13. 文笔画像与语言习惯",
    "SENTENCES": "## 14. 常用词、句式与可复用表达提取",
    "CITATIONS": "## 15. 引用策略与文献使用",
}

BACK_MATTER_RE = re.compile(
    r"\b("
    r"references|acknowledg(e)?ments?|declaration|credit|data availability|"
    r"appendix|supplementary|nomenclature|author contributions?"
    r")\b",
    flags=re.I,
)

BODY_EXCLUDE_RE = re.compile(
    r"\b("
    r"abstract|keywords|article info|nomenclature|abbreviations|received|accepted|"
    r"available online|journal homepage|contents lists available|copyright|all rights reserved|"
    r"elsevier|springer|wiley|sciencedirect|correspondence|e-mail|email|doi|https?://|www\."
    r")\b",
    flags=re.I,
)

KNOWN_JOURNAL_PHRASES = [
    "Aerospace Science and Technology",
    "Composite Structures",
    "Composites Part B",
    "Computer Methods in Applied Mechanics and Engineering",
    "International Journal of Heat and Mass Transfer",
    "International Journal of Thermal Sciences",
    "Probabilistic Engineering Mechanics",
    "Applied Thermal Engineering",
    "Acta Astronautica",
    "Chinese Journal of Aeronautics",
    "Materials & Design",
    "Journal of Fluids and Structures",
    "Journal of Alloys and Compounds",
    "Journal of the European Ceramic Society",
    "Structural Safety",
]

STOPWORDS = {
    "about",
    "above",
    "after",
    "again",
    "against",
    "almost",
    "also",
    "although",
    "among",
    "and",
    "another",
    "are",
    "around",
    "based",
    "because",
    "been",
    "before",
    "being",
    "between",
    "both",
    "can",
    "could",
    "did",
    "does",
    "during",
    "each",
    "for",
    "from",
    "had",
    "has",
    "have",
    "having",
    "here",
    "however",
    "into",
    "its",
    "may",
    "more",
    "most",
    "not",
    "only",
    "other",
    "our",
    "paper",
    "present",
    "proposed",
    "respectively",
    "result",
    "results",
    "same",
    "several",
    "show",
    "shown",
    "shows",
    "such",
    "than",
    "that",
    "the",
    "their",
    "then",
    "there",
    "these",
    "this",
    "those",
    "through",
    "thus",
    "under",
    "using",
    "used",
    "uses",
    "was",
    "were",
    "when",
    "where",
    "which",
    "while",
    "with",
    "within",
    "would",
}

BANNED_TOKENS = {
    "aip",
    "all",
    "author",
    "authors",
    "available",
    "chen",
    "connor",
    "copyright",
    "crossref",
    "deg",
    "ding",
    "doi",
    "elsevier",
    "email",
    "fig",
    "figure",
    "fwm",
    "gao",
    "gong",
    "gpa",
    "homepage",
    "huang",
    "http",
    "https",
    "journal",
    "li",
    "liu",
    "mpa",
    "online",
    "page",
    "pdf",
    "received",
    "revell",
    "reserved",
    "rights",
    "rveb",
    "rvem",
    "sciencedirect",
    "source",
    "sts",
    "su",
    "supplement",
    "table",
    "tavg",
    "tmax",
    "unif",
    "var",
    "wang",
    "xhf",
    "xwf",
    "xwh",
    "xref",
    "yang",
    "yu",
    "zhang",
}

BANNED_NGRAM_TERMS = BANNED_TOKENS | {
    "acknowledgments",
    "acknowledgements",
    "appendix",
    "declaration",
    "references",
    "supplementary",
}

NOUN_HINTS = ("tion", "sion", "ment", "ness", "ity", "ics", "ure", "ance", "ence", "ship", "ism")
ADJ_HINTS = ("al", "ive", "ous", "ic", "ical", "ary", "able", "ible", "less", "ant", "ent")
ACADEMIC_VERBS = {
    "achieve",
    "achieved",
    "analyze",
    "analyzed",
    "compare",
    "compared",
    "construct",
    "constructed",
    "demonstrate",
    "demonstrated",
    "derive",
    "derived",
    "develop",
    "developed",
    "enable",
    "enabled",
    "estimate",
    "estimated",
    "evaluate",
    "evaluated",
    "identify",
    "identified",
    "indicate",
    "indicated",
    "optimize",
    "optimized",
    "predict",
    "predicted",
    "present",
    "presented",
    "propose",
    "proposed",
    "provide",
    "provided",
    "reveal",
    "revealed",
    "show",
    "shown",
    "validate",
    "validated",
}


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_space(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = text.replace("颅", "")
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_old_blocks(report: str) -> str:
    patterns = [
        r"\n?<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->.*?<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->\s*",
        r"\n?<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->.*?<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->\s*",
        r"\n?" + re.escape(LEGACY_REAUDIT_START) + r".*?" + re.escape(LEGACY_REAUDIT_END) + r"\s*",
        r"\n?<!-- REAUDIT-INTEGRATED-2026-05-26:[A-Z_]+ START -->.*?<!-- REAUDIT-INTEGRATED-2026-05-26:[A-Z_]+ END -->\s*",
    ]
    for pattern in patterns:
        report = re.sub(pattern, "\n", report, flags=re.S)
    report = re.sub(r"\n{3,}", "\n\n", report)
    return report.strip() + "\n"


def marker(name: str, body: str) -> str:
    return (
        f"<!-- {INTEGRATED_PREFIX}:{name} START -->\n"
        f"{body.strip()}\n"
        f"<!-- {INTEGRATED_PREFIX}:{name} END -->"
    )


def insert_before_next_h2(report: str, heading: str, block: str) -> str:
    match = re.search(rf"^{re.escape(heading)}\s*$", report, flags=re.M)
    if not match:
        return report.rstrip() + "\n\n" + block.strip() + "\n"
    next_match = re.search(r"^## \d+\. ", report[match.end() :], flags=re.M)
    insert_at = match.end() + next_match.start() if next_match else len(report)
    before = report[:insert_at].rstrip()
    after = report[insert_at:].lstrip("\n")
    return before + "\n\n" + block.strip() + "\n\n" + after


def block_quote(text: str) -> str:
    if not text.strip():
        return "> 未识别。"
    return "\n".join(("> " + line) if line.strip() else ">" for line in text.strip().splitlines())


def format_pairs(pairs: Iterable[tuple[str, int]] | Iterable[tuple[tuple[str, ...], int]]) -> str:
    out = []
    for key, count in pairs:
        if isinstance(key, tuple):
            key = " ".join(key)
        out.append(f"{key}({count})")
    return "；".join(out) if out else "未稳定识别"


def sentence_split(text: str) -> list[str]:
    text = normalize_space(re.sub(r"\s+", " ", text))
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
    return [p.strip() for p in parts if 45 <= len(p.strip()) <= 450]


def tail_of_section(text: str, max_sentences: int = 5) -> str:
    cleaned = clean_body_text(text)
    sentences = sentence_split(cleaned)
    if sentences:
        return " ".join(sentences[-max_sentences:])
    return cleaned[-1800:].strip()


def pick_sentences(sentences: list[str], keywords: Iterable[str], limit: int = 5) -> list[str]:
    kws = [k.lower() for k in keywords]
    output = []
    for sentence in sentences:
        lower = sentence.lower()
        if any(k in lower for k in kws) and not is_non_body_line(sentence):
            output.append(sentence)
        if len(output) >= limit:
            break
    return output


def make_template(sentence: str) -> str:
    template = re.sub(r"\b\d+(?:\.\d+)?\s*%?", "X", sentence)
    template = re.sub(r"\b[A-Z]{2,}(?:-[A-Z]{2,})?\b", "METHOD", template)
    template = re.sub(r"\bthe proposed [A-Za-z\- ]+? method\b", "the proposed METHOD", template, flags=re.I)
    template = re.sub(r"\bhypersonic flight vehicles?\b", "TARGET SYSTEM", template, flags=re.I)
    return template


def is_back_matter(title: str) -> bool:
    return bool(BACK_MATTER_RE.search(title))


def is_non_body_line(text: str) -> bool:
    raw = normalize_space(text)
    lower = raw.lower()
    if not raw:
        return True
    if BODY_EXCLUDE_RE.search(raw):
        return True
    if re.match(r"^(fig\.|figure|table)\s*\d+", raw, flags=re.I):
        return True
    if re.search(r"\bet al\.\s+.*\b(19|20)\d{2}\b", raw) and len(raw.split()) < 28:
        return True
    if any(phrase.lower() in lower for phrase in KNOWN_JOURNAL_PHRASES) and len(raw.split()) < 35:
        return True
    if len(re.findall(r"\d", raw)) > max(8, len(raw) // 4):
        return True
    if len(raw) < 12:
        return True
    return False


def clean_body_text(text: str) -> str:
    text = normalize_space(text)
    for phrase in KNOWN_JOURNAL_PHRASES:
        text = re.sub(re.escape(phrase), " ", text, flags=re.I)
    text = re.sub(r"\b[A-Z]\.\s+[A-Z][A-Za-z]+ et al\.\s+[^.\n]{0,120}\b(?:19|20)\d{2}\b[^.\n]{0,80}", " ", text)
    text = re.sub(r"\b(?:Fig\.|Figure|Table)\s*\d+[^\n.]{0,260}", " ", text, flags=re.I)
    text = re.sub(r"\b(?:Received|Accepted|Available online)\b[^.\n]{0,220}", " ", text, flags=re.I)
    text = re.sub(r"https?://\S+|www\.\S+|\bdoi:\S+", " ", text, flags=re.I)
    lines = []
    for line in text.splitlines():
        if not is_non_body_line(line):
            lines.append(line)
    if not lines:
        lines = [part for part in re.split(r"(?<=[.!?])\s+", text) if not is_non_body_line(part)]
    cleaned = " ".join(lines)
    replacements = {
        r"\bcoe\s+cient(s)?\b": "coefficient",
        r"\bef\s+ciency\b": "efficiency",
        r"\bdi\s+erent\b": "different",
        r"\bﬂight\b": "flight",
        r"\bight\b": "flight",
        r"\bthermo\s+electric\b": "thermoelectric",
    }
    for pattern, repl in replacements.items():
        cleaned = re.sub(pattern, repl, cleaned, flags=re.I)
    return normalize_space(cleaned)


def clean_abstract_text(text: str) -> str:
    text = normalize_space(text)
    text = re.split(r"\b1\.?\s+Introduction\b", text, maxsplit=1, flags=re.I)[0]
    text = re.split(r"\bKeywords?\s*:", text, maxsplit=1, flags=re.I)[0]
    parts = re.split(r"(?<=[.!?])\s+(?=(?:or|and|but|for|where|while)\s+[a-z])", text, maxsplit=1)
    if parts and len(parts[0]) >= 120:
        text = parts[0]
    return normalize_space(text)


def body_section_indices(toc: list[dict]) -> list[int]:
    indices = []
    for idx, item in enumerate(toc):
        title = item.get("title", "")
        level = int(item.get("level", 2))
        if is_back_matter(title):
            continue
        if level != 2:
            continue
        if re.match(r"^\d+(?:\.\d+)*\.?\s+", title) or re.search(
            r"\b(introduction|method|model|formulation|problem|results?|discussion|validation|case|conclusions?)\b",
            title,
            flags=re.I,
        ):
            indices.append(idx)
    return indices


def extract_body_sections(pdf_path: Path, text: str, toc: list[dict]) -> tuple[str, dict[str, str], list[str]]:
    section_texts: dict[str, str] = {}
    warnings: list[str] = []
    for idx in body_section_indices(toc):
        title = toc[idx].get("title", f"section-{idx}")
        section = ""
        ok = False
        if pdf_path.exists():
            section, ok = legacy.extract_pdf_section(pdf_path, toc, idx)
        if not ok or len(section) < 80:
            section, ok = legacy.extract_by_toc(text, toc, idx)
        cleaned = clean_body_text(section)
        if len(cleaned) >= 80:
            section_texts[title] = cleaned
        else:
            warnings.append(f"{title}: 正文抽取偏短")
    if not section_texts:
        front = re.split(r"\n\s*References\b", legacy.strip_page_markers(text), flags=re.I)[0]
        section_texts["正文候选区"] = clean_body_text(front)
        warnings.append("未能按 TOC 稳定切分正文，使用 References 之前的候选正文区。")
    return "\n\n".join(section_texts.values()), section_texts, warnings


def tokenize(text: str) -> list[str]:
    raw_tokens = re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text)
    tokens: list[str] = []
    for token in raw_tokens:
        word = token.lower().strip("-")
        if word in STOPWORDS or word in BANNED_TOKENS:
            continue
        if len(word.replace("-", "")) < 3 or re.fullmatch(r"[a-z]{1,2}\d+", word):
            continue
        if re.match(r"^[a-z]-", word):
            continue
        if re.fullmatch(r"(sin|cos|tan|log|exp|xref|unif|non-unif|elems?)", word):
            continue
        tokens.append(word)
    return tokens


def valid_ngram(words: tuple[str, ...]) -> bool:
    if len(set(words)) != len(words):
        return False
    if any(word in BANNED_NGRAM_TERMS for word in words):
        return False
    phrase = " ".join(words)
    banned_phrases = {
        "aerospace science technology",
        "computer methods applied",
        "applied mechanics engineering",
        "probabilistic engineering mechanics",
        "international journal heat",
        "journal heat mass",
        "elsevier masson sas",
        "masson sas all",
        "all rights reserved",
    }
    if phrase in banned_phrases:
        return False
    if re.search(r"\b(?:science technology|mechanics engineering|mass transfer fig|structures fig)\b", phrase):
        return False
    if any(word.endswith("pdf") or word.startswith("xref") for word in words):
        return False
    return True


def ngram_counts(words: list[str], n: int, limit: int = 12) -> list[tuple[str, int]]:
    counter = Counter()
    for idx in range(0, max(0, len(words) - n + 1)):
        gram = tuple(words[idx : idx + n])
        if valid_ngram(gram):
            counter[gram] += 1
    return [(" ".join(key), value) for key, value in counter.most_common(limit)]


def stats_for_body(body_text: str, section_texts: dict[str, str]) -> dict:
    words = tokenize(body_text)
    word_counter = Counter(words)
    nouns = Counter(w for w in words if any(w.endswith(suf) for suf in NOUN_HINTS))
    adjs = Counter(w for w in words if any(w.endswith(suf) for suf in ADJ_HINTS))
    advs = Counter(w for w in words if w.endswith("ly"))
    verbs = Counter(w for w in words if w in ACADEMIC_VERBS)
    passive = len(re.findall(r"\b(?:is|are|was|were|be|been|being)\s+\w+ed\b", body_text, flags=re.I))
    we_active = len(
        re.findall(
            r"\bwe\s+(?:propose|develop|present|show|demonstrate|derive|use|construct|introduce|validate)\b",
            body_text,
            flags=re.I,
        )
    )
    present = len(re.findall(r"\b(?:is|are|shows?|indicates?|suggests?|demonstrates?|provides?|enables?)\b", body_text, flags=re.I))
    past = len(re.findall(r"\b(?:was|were|\w+ed)\b", body_text, flags=re.I))
    perfect = len(re.findall(r"\b(?:has|have)\s+\w+ed\b", body_text, flags=re.I))
    modal = len(re.findall(r"\b(?:may|might|can|could|should|would)\b", body_text, flags=re.I))
    section_freq = {
        name: Counter(tokenize(value)).most_common(8)
        for name, value in section_texts.items()
        if value and len(tokenize(value)) >= 15
    }
    return {
        "source": "body_only_no_abstract_references_captions_headers",
        "body_chars": len(body_text),
        "top_words": word_counter.most_common(20),
        "top_nouns": nouns.most_common(15),
        "top_verbs": verbs.most_common(15),
        "top_adjs": adjs.most_common(15),
        "top_advs": advs.most_common(15),
        "top_bigrams": ngram_counts(words, 2, 12),
        "top_trigrams": ngram_counts(words, 3, 12),
        "passive_estimate": passive,
        "we_active_estimate": we_active,
        "present_estimate": present,
        "past_estimate": past,
        "perfect_estimate": perfect,
        "modal_estimate": modal,
        "section_freq": section_freq,
    }


def classify_heading_cn(title: str) -> str:
    lower = title.lower()
    if "introduction" in lower:
        return "背景定位/文献缺口"
    if any(key in lower for key in ["method", "model", "framework", "formulation", "algorithm", "approach"]):
        return "方法/模型/算法"
    if any(key in lower for key in ["problem", "description"]):
        return "问题定义"
    if any(key in lower for key in ["result", "discussion", "validation", "case", "experiment", "application"]):
        return "结果/验证/讨论"
    if "conclusion" in lower:
        return "结论/贡献回收"
    if is_back_matter(title):
        return "尾部材料"
    return "对象/模块/过渡章节"


def toc_markdown(toc: list[dict]) -> tuple[str, str]:
    tree = []
    table = [
        "| 章节/小节名 | 页码 | 层级 | 功能判断 |",
        "| --- | ---: | ---: | --- |",
    ]
    for item in toc:
        title = item.get("title", "").strip()
        level = int(item.get("level", 2))
        if level == 1:
            continue
        safe_title = title.replace("|", "\\|")
        indent = "  " * max(0, level - 2)
        tree.append(f"{indent}- L{level} p.{item.get('page', '?')}: {title}（{classify_heading_cn(title)}）")
        table.append(
            f"| {safe_title} | {item.get('page', '?')} | {level} | {classify_heading_cn(title)} |"
        )
    return "\n".join(tree) if tree else "- 未从 metadata 中识别到 TOC。", "\n".join(table)


def load_cached_translation(cache: dict[str, str], old_evidence: dict, stem: str, field: str, source_text: str, translate: bool) -> str:
    source_text = normalize_space(source_text)
    source_hash = hashlib.sha1(source_text.encode("utf-8")).hexdigest()[:12]
    key = f"{stem}::{field}::{source_hash}"
    old_value = old_evidence.get(f"{field}_zh", "")
    old_source = normalize_space(old_evidence.get(field, ""))
    if (
        old_source == source_text
        and old_value
        and "未启用自动翻译" not in old_value
        and "自动翻译失败" not in old_value
    ):
        cache[key] = old_value
        return old_value
    return legacy.translate_google(source_text, cache, key, translate)


def extract_core(record: dict, meta: dict, text: str, translate: bool, cache: dict[str, str]) -> dict:
    stem = record["stem"]
    toc = meta.get("toc") or record.get("toc") or legacy.infer_toc_from_text(text)
    pdf_path = PDF_DIR / record.get("pdf_name", f"{stem}.pdf")
    old_path = EVIDENCE_DIR / f"{stem}.json"
    old_evidence = read_json(old_path) if old_path.exists() else {}

    if pdf_path.exists():
        abstract, abstract_ok = legacy.extract_pdf_abstract(pdf_path)
        if not abstract_ok or len(abstract) < 80:
            abstract, abstract_ok = legacy.extract_abstract(text, toc, meta.get("keywords") or record.get("keywords"))
    else:
        abstract, abstract_ok = legacy.extract_abstract(text, toc, meta.get("keywords") or record.get("keywords"))
    abstract = clean_abstract_text(abstract)

    conclusion_heading, conclusion, conclusion_ok = legacy.find_conclusion(toc, text)
    if pdf_path.exists():
        conclusion_indices = [
            i
            for i, item in enumerate(toc)
            if re.search(r"\bconclusions?\b|\bconcluding remarks\b", item.get("title", ""), flags=re.I)
        ]
        for idx in conclusion_indices:
            pdf_conclusion, pdf_ok = legacy.extract_pdf_section(pdf_path, toc, idx)
            if pdf_ok and len(pdf_conclusion) > 80:
                conclusion_heading = toc[idx]["title"]
                conclusion = pdf_conclusion
                conclusion_ok = True
                break
        if not conclusion or len(conclusion) < 80:
            discussion_indices = [
                i
                for i, item in enumerate(toc)
                if re.search(r"\bdiscussion\b", item.get("title", ""), flags=re.I)
            ]
            for idx in reversed(discussion_indices):
                pdf_discussion, pdf_ok = legacy.extract_pdf_section(pdf_path, toc, idx)
                discussion_tail = tail_of_section(pdf_discussion) if pdf_ok else ""
                if len(discussion_tail) > 80:
                    conclusion_heading = toc[idx]["title"] + "（无独立 Conclusion，取 Discussion 末段）"
                    conclusion = discussion_tail
                    conclusion_ok = False
                    break

    if pdf_path.exists():
        references_block, references = legacy.extract_pdf_references(pdf_path)
        if not references:
            references_block, references = legacy.extract_references(text)
    else:
        references_block, references = legacy.extract_references(text)

    intro = ""
    intro_idx = next((i for i, item in enumerate(toc) if re.search(r"\bIntroduction\b", item.get("title", ""), flags=re.I)), None)
    if intro_idx is not None:
        if pdf_path.exists():
            intro, _ = legacy.extract_pdf_section(pdf_path, toc, intro_idx)
        if len(intro) < 80:
            intro, _ = legacy.extract_by_toc(text, toc, intro_idx)

    body_text, body_sections, body_warnings = extract_body_sections(pdf_path, text, toc)
    body_stats = stats_for_body(body_text, body_sections)
    subject = meta.get("subject") or record.get("subject") or ""
    journal_hint = subject.split(",")[0].strip() if "," in subject else ""
    cites = legacy.citation_analysis(text, intro, references, journal_hint)
    logic = legacy.infer_logic(abstract, intro, conclusion)
    sentences = sentence_split(" ".join([abstract, intro, conclusion]))
    sentence_groups = {
        "背景/问题定位句": pick_sentences(sentences, ["important", "essential", "critical", "requires", "challenge"], 5),
        "Gap/转折句": pick_sentences(sentences, ["however", "limited", "lack", "remain", "few", "difficult"], 5),
        "方法提出句": pick_sentences(sentences, ["propose", "develop", "present", "method", "model", "framework", "approach"], 5),
        "结果呈现句": pick_sentences(sentences, ["results", "show", "demonstrate", "achieve", "indicate", "outperform"], 5),
        "贡献/增量句": pick_sentences(sentences, ["provide", "enable", "reveal", "establish", "contribute", "improve"], 5),
        "限制/边界句": pick_sentences(sentences, ["may", "could", "limited", "only", "future", "should"], 5),
    }
    abstract_zh = load_cached_translation(cache, old_evidence, stem, "abstract", abstract, translate)
    conclusion_zh = load_cached_translation(cache, old_evidence, stem, "conclusion", conclusion, translate)

    return {
        "stem": stem,
        "title": meta.get("title") or record.get("title") or stem,
        "toc": toc,
        "abstract": abstract,
        "abstract_ok": abstract_ok,
        "abstract_zh": abstract_zh,
        "conclusion_heading": conclusion_heading,
        "conclusion": conclusion,
        "conclusion_ok": conclusion_ok,
        "conclusion_zh": conclusion_zh,
        "intro": intro,
        "references": references,
        "reference_count": len(references),
        "citation_analysis": cites,
        "logic": logic,
        "body_stats": body_stats,
        "body_stats_warnings": body_warnings,
        "body_section_names": list(body_sections),
        "sentence_groups": sentence_groups,
    }


def local_evidence_note(stem: str, field: str) -> str:
    label = "摘要" if field == "abstract" else "结论"
    return (
        f"完整英文{label}原文不在公开报告正文中展开；本地完整摘录见 "
        f"`801/深度拆解/extracted_evidence/{stem}.json` 的 `{field}` 字段，"
        f"以及 `801/深度拆解/local_full_reports/{stem}.md`。"
    )


def build_blocks(data: dict) -> dict[str, str]:
    toc_tree, toc_table = toc_markdown(data["toc"])
    cites = data["citation_analysis"]
    stats = data["body_stats"]
    logic = data["logic"]
    sentence_lines = []
    for group, examples in data["sentence_groups"].items():
        sentence_lines.append(f"#### {group}")
        if not examples:
            sentence_lines.append("- 未在摘要/引言/结论中稳定识别；正式使用时从对应章节人工补足。")
            continue
        for sentence in examples:
            sentence_lines.append(f"- 原句：{sentence}")
            sentence_lines.append(f"  可迁移模板：{make_template(sentence)}")

    gap_lines = cites.get("gap_citation_sentences") or []
    gap_md = "\n".join(f"- {line}" for line in gap_lines) if gap_lines else "- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。"
    references = data.get("references", [])[:8]
    ref_md = "\n".join(f"- {ref}" for ref in references) if references else "- 未解析出结构化参考文献条目。"
    section_freq_md = "\n".join(
        f"- {section}: {format_pairs(freqs)}"
        for section, freqs in stats["section_freq"].items()
    )
    if not section_freq_md:
        section_freq_md = "- 正文章节词频未稳定识别。"
    body_warning_md = "\n".join(f"- {item}" for item in data["body_stats_warnings"]) if data["body_stats_warnings"] else "- 无明显正文切分告警。"

    return {
        "STATUS": marker(
            "STATUS",
            f"""### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：{', '.join(data['body_section_names']) if data['body_section_names'] else '未稳定识别'}。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
{body_warning_md}""",
        ),
        "ABSTRACT": marker(
            "ABSTRACT",
            f"""### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：{'成功' if data['abstract_ok'] else '未稳定识别，需要回 PDF 首页复核'}。
- {local_evidence_note(data['stem'], 'abstract')}

中文译文：

{block_quote(data['abstract_zh'])}""",
        ),
        "LOGIC": marker(
            "LOGIC",
            f"""### 复核补充：问题-方法-增量闭环

- 提出的问题：{logic['problem']}
- 已有研究不足/GAP：{logic['gap']}
- 本文解决方式：{logic['method']}
- 学术或工程增量：{logic['increment']}
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。""",
        ),
        "STRUCTURE": marker(
            "STRUCTURE",
            f"""### 复核补充：严格章节树与章节名功能

严格章节树：

{toc_tree}

章节名功能表：

{toc_table}""",
        ),
        "LANGUAGE": marker(
            "LANGUAGE",
            f"""### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：{stats['body_chars']}
- 高频词：{format_pairs(stats['top_words'])}
- 高频名词化/学术名词：{format_pairs(stats['top_nouns'])}
- 高频学术动词：{format_pairs(stats['top_verbs'])}
- 高频形容词：{format_pairs(stats['top_adjs'])}
- 高频副词：{format_pairs(stats['top_advs'])}
- 高频二词短语：{format_pairs(stats['top_bigrams'])}
- 高频三词短语：{format_pairs(stats['top_trigrams'])}
- 被动语态估计：{stats['passive_estimate']}；`we + 动作动词` 主动句估计：{stats['we_active_estimate']}
- 一般现在时线索：{stats['present_estimate']}；一般过去时线索：{stats['past_estimate']}；现在完成时线索：{stats['perfect_estimate']}；情态动词线索：{stats['modal_estimate']}

分章节正文词频：

{section_freq_md}""",
        ),
        "SENTENCES": marker(
            "SENTENCES",
            f"""### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

{chr(10).join(sentence_lines)}""",
        ),
        "CITATIONS": marker(
            "CITATIONS",
            f"""### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：{cites['in_text_citation_clusters']}
- Introduction 引文簇数量估计：{cites['intro_citation_clusters']}
- References 条目数：{cites['reference_count']}
- 可识别年份条目数：{cites['reference_year_count']}
- 2021 年及以后文献数：{cites['recent_2021_plus']}
- 2010 年前经典文献数：{cites['classic_pre_2010']}
- 同刊引用数（按 subject 粗匹配）：{cites['same_journal_refs']}
- 高频来源期刊：{format_pairs(cites['top_journals'])}
- 引文簇样例：{', '.join(cites['sample_clusters'][:12]) if cites['sample_clusters'] else '未识别'}

带引文的 gap/转折句样例：

{gap_md}

References 解析样例（前 8 条）：

{ref_md}""",
        ),
    }


def integrate_report(report: str, blocks: dict[str, str]) -> str:
    report = strip_old_blocks(report)
    for key in ["STATUS", "ABSTRACT", "LOGIC", "STRUCTURE", "LANGUAGE", "SENTENCES", "CITATIONS"]:
        report = insert_before_next_h2(report, TARGET_HEADINGS[key], blocks[key])
    return report.rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge 801 reaudit material into the main per-paper report sections.")
    parser.add_argument("--translate", action="store_true", help="Call the public Google Translate endpoint for missing cached translations.")
    parser.add_argument("--limit", type=int, default=0, help="Process only the first N records.")
    parser.add_argument("--start", type=int, default=0, help="Zero-based manifest offset for chunked runs.")
    args = parser.parse_args()

    manifest = read_json(MANIFEST)
    end = args.start + args.limit if args.limit else None
    records = manifest[args.start : end]
    cache = legacy.translation_cache() if TRANSLATION_CACHE.exists() else {}
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    processed = 0
    failures: list[str] = []
    for record in records:
        stem = record["stem"]
        txt_path = TEXT_DIR / f"{stem}.txt"
        meta_path = META_DIR / f"{stem}.json"
        report_path = REPORT_DIR / f"{stem}.md"
        if not txt_path.exists() or not meta_path.exists() or not report_path.exists():
            failures.append(f"{stem}: missing input/report")
            continue
        text = txt_path.read_text(encoding="utf-8", errors="replace")
        meta = read_json(meta_path)
        data = extract_core(record, meta, text, args.translate, cache)
        blocks = build_blocks(data)
        report = report_path.read_text(encoding="utf-8", errors="replace")
        report_path.write_text(integrate_report(report, blocks), encoding="utf-8")
        evidence = {
            "stem": data["stem"],
            "title": data["title"],
            "abstract_ok": data["abstract_ok"],
            "abstract": data["abstract"],
            "abstract_zh": data["abstract_zh"],
            "conclusion_heading": data["conclusion_heading"],
            "conclusion_ok": data["conclusion_ok"],
            "conclusion": data["conclusion"],
            "conclusion_zh": data["conclusion_zh"],
            "toc": data["toc"],
            "reference_count": data["reference_count"],
            "citation_analysis": data["citation_analysis"],
            "logic": data["logic"],
            "body_stats": data["body_stats"],
            "body_stats_warnings": data["body_stats_warnings"],
            "body_section_names": data["body_section_names"],
            "sentence_groups": data["sentence_groups"],
        }
        (EVIDENCE_DIR / f"{stem}.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
        processed += 1
        legacy.save_translation_cache(cache)
        print(f"[{processed}/{len(records)}] {stem}", flush=True)

    legacy.save_translation_cache(cache)
    print(f"processed={processed} failures={len(failures)} translate={args.translate}")
    if failures:
        print("\n".join(failures))


if __name__ == "__main__":
    main()
