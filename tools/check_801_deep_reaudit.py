from __future__ import annotations

import json
import re
from pathlib import Path


BASE = Path("801") / "深度拆解"
EVIDENCE_DIR = BASE / "extracted_evidence"
REPORT_DIR = BASE / "papers"
MANIFEST = Path("801") / "文本" / "_manifest.json"

REQUIRED_MARKERS = [
    "<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->",
    "<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->",
    "<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->",
    "<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->",
    "<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->",
    "<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->",
    "<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->",
]

REQUIRED_HEADINGS = [
    "## 0. 读取说明",
    "## 2. 摘要与核心信息提取",
    "## 7. 论证链条复原",
    "## 11. 章节结构与篇章布局",
    "## 13. 文笔画像与语言习惯",
    "## 14. 常用词、句式与可复用表达提取",
    "## 15. 引用策略与文献使用",
]

BAD_REPORT_PATTERNS = [
    "## 20. 复核增强",
    "<!-- REAUDIT-2026-05-26 START -->",
    "<!-- AUTO-AUGMENT:",
]

BAD_TRIGRAM_SUBSTRINGS = [
    "page ",
    " fig",
    "figure",
    " table",
    "journal",
    "homepage",
    "elsevier",
    "rights reserved",
    "source pdf",
    "pdf extracted",
    "extracted extraction",
    "aerospace science technology",
    "science technology fig",
    "computer methods applied",
    "applied mechanics engineering",
    "probabilistic engineering mechanics",
    "international journal heat",
    "journal heat mass",
    "gpa gpa",
    "mpa mpa",
    "xref xref",
    "cos cos",
    "sin cos",
    "unif unif",
    "zhang zhang",
    "zhang gong",
    "connor revell",
    "xwh",
    "xwf",
    "xhf",
    "tavg",
    "tmax",
    "fwm",
    "sts ats",
    "european ceramic society",
]


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def bad_trigram_line(line: str) -> list[str]:
    lower = line.lower()
    problems = [item for item in BAD_TRIGRAM_SUBSTRINGS if item in lower]
    repeated = re.findall(r"\b([a-z][a-z-]{2,})\s+\1\s+\1\(", lower)
    problems.extend(f"repeated:{item}" for item in repeated)
    return problems


def check_report_text(text: str) -> list[str]:
    problems = []
    for marker in REQUIRED_MARKERS:
        if marker not in text:
            problems.append(f"missing marker {marker}")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            problems.append(f"missing heading {heading}")
    for pattern in BAD_REPORT_PATTERNS:
        if pattern in text:
            problems.append(f"legacy block remains: {pattern}")
    for line in text.splitlines():
        if "高频三词短语：" in line:
            bad = bad_trigram_line(line)
            if bad:
                problems.append(f"bad trigram line: {', '.join(bad)}")
    return problems


def check_evidence(data: dict) -> list[str]:
    flags = []
    if not data.get("abstract_ok") or len(data.get("abstract", "")) < 80:
        flags.append("abstract")
    if (
        len(data.get("abstract_zh", "")) < 40
        or "未启用自动翻译" in data.get("abstract_zh", "")
        or "自动翻译失败" in data.get("abstract_zh", "")
    ):
        flags.append("abstract_zh")
    if len(data.get("conclusion", "")) < 80:
        flags.append("conclusion")
    if (
        len(data.get("conclusion_zh", "")) < 40
        or "未启用自动翻译" in data.get("conclusion_zh", "")
        or "自动翻译失败" in data.get("conclusion_zh", "")
    ):
        flags.append("conclusion_zh")
    if len(data.get("toc", [])) < 3:
        flags.append("toc")
    if data.get("reference_count", 0) < 10:
        flags.append("references")
    stats = data.get("body_stats", {})
    if stats.get("source") != "body_only_no_abstract_references_captions_headers":
        flags.append("body_stats_source")
    for trigram, _count in stats.get("top_trigrams", []):
        bad = bad_trigram_line(f"高频三词短语：{trigram}(1)")
        words = trigram.lower().split()
        if len(words) == 3 and len(set(words)) != 3:
            bad.append("duplicated-token")
        if bad:
            flags.append(f"bad_trigram:{trigram}")
    return flags


def main() -> None:
    manifest = read_json(MANIFEST)
    rows = []
    missing_reports = []
    missing_evidence = []
    report_problems = []
    extraction_problems = []

    for record in manifest:
        stem = record["stem"]
        report_path = REPORT_DIR / f"{stem}.md"
        evidence_path = EVIDENCE_DIR / f"{stem}.json"
        if not report_path.exists():
            missing_reports.append(stem)
            continue
        if not evidence_path.exists():
            missing_evidence.append(stem)
            continue
        report_text = report_path.read_text(encoding="utf-8", errors="replace")
        report_flags = check_report_text(report_text)
        if report_flags:
            report_problems.append((stem, report_flags))
        data = read_json(evidence_path)
        evidence_flags = check_evidence(data)
        if evidence_flags:
            extraction_problems.append((stem, evidence_flags))
        stats = data.get("body_stats", {})
        rows.append(
            {
                "stem": stem,
                "abstract_chars": len(data.get("abstract", "")),
                "conclusion_chars": len(data.get("conclusion", "")),
                "reference_count": data.get("reference_count", 0),
                "toc_count": len(data.get("toc", [])),
                "body_chars": stats.get("body_chars", 0),
                "flags": ",".join(evidence_flags) if evidence_flags else "ok",
            }
        )

    lines = [
        "# 801 Deep Reaudit Quality Report",
        "",
        "Scope: integrated per-paper reports with body-only frequency/trigram checks.",
        "",
        f"Expected papers: {len(manifest)}",
        f"Reports present: {len(list(REPORT_DIR.glob('*.md')))}",
        f"Evidence files: {len(list(EVIDENCE_DIR.glob('*.json')))}",
        f"Missing reports: {len(missing_reports)}",
        f"Missing evidence: {len(missing_evidence)}",
        f"Reports with problems: {len(report_problems)}",
        f"Evidence extraction problems: {len(extraction_problems)}",
        "",
        "## Per-Paper Checks",
        "",
        "| Stem | Abstract chars | Conclusion chars | References | TOC items | Body chars | Evidence flags |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['stem']}` | {row['abstract_chars']} | {row['conclusion_chars']} | "
            f"{row['reference_count']} | {row['toc_count']} | {row['body_chars']} | {row['flags']} |"
        )

    lines.extend(["", "## Missing Reports", ""])
    lines.append("None." if not missing_reports else "\n".join(f"- `{item}`" for item in missing_reports))
    lines.extend(["", "## Missing Evidence", ""])
    lines.append("None." if not missing_evidence else "\n".join(f"- `{item}`" for item in missing_evidence))
    lines.extend(["", "## Report Problems", ""])
    if report_problems:
        for stem, flags in report_problems:
            lines.append(f"- `{stem}`: {'; '.join(flags)}")
    else:
        lines.append("None.")
    lines.extend(["", "## Evidence Problems", ""])
    if extraction_problems:
        for stem, flags in extraction_problems:
            lines.append(f"- `{stem}`: {', '.join(flags)}")
    else:
        lines.append("None.")

    out = BASE / "_reaudit_quality_report.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(
        f"missing_reports={len(missing_reports)} missing_evidence={len(missing_evidence)} "
        f"report_problems={len(report_problems)} extraction_problems={len(extraction_problems)}"
    )


if __name__ == "__main__":
    main()
