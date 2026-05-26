from __future__ import annotations

import json
from pathlib import Path


BASE = Path("801") / "深度拆解"
EVIDENCE_DIR = BASE / "extracted_evidence"
REPORT_DIR = BASE / "papers"
MANIFEST = Path("801") / "文本" / "_manifest.json"

REQUIRED_STRINGS = [
    "<!-- REAUDIT-2026-05-26 START -->",
    "### 20.1 严格章节树",
    "### 20.3 摘要完整摘录",
    "### 20.4 摘要中文翻译",
    "### 20.5 结论完整摘录",
    "### 20.6 结论中文翻译",
    "### 20.7 论文逻辑脉络复核",
    "### 20.8 引文分析补全",
    "### 20.9 常用词、词类、语态与时态",
    "### 20.10 句型库扩充",
]


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
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
        absent = [item for item in REQUIRED_STRINGS if item not in report_text]
        if absent:
            report_problems.append((stem, absent))
        data = json.loads(evidence_path.read_text(encoding="utf-8"))
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
        if flags:
            extraction_problems.append((stem, flags))
        rows.append(
            {
                "stem": stem,
                "abstract_chars": len(data.get("abstract", "")),
                "conclusion_chars": len(data.get("conclusion", "")),
                "reference_count": data.get("reference_count", 0),
                "toc_count": len(data.get("toc", [])),
                "flags": ",".join(flags) if flags else "ok",
            }
        )

    lines = [
        "# 801 Deep Reaudit Quality Report",
        "",
        f"Expected papers: {len(manifest)}",
        f"Reports present: {len(list(REPORT_DIR.glob('*.md')))}",
        f"Evidence files: {len(list(EVIDENCE_DIR.glob('*.json')))}",
        f"Missing reports: {len(missing_reports)}",
        f"Missing evidence: {len(missing_evidence)}",
        f"Reports with missing required strings: {len(report_problems)}",
        f"Evidence extraction problems: {len(extraction_problems)}",
        "",
        "## Per-Paper Checks",
        "",
        "| Stem | Abstract chars | Conclusion chars | References | TOC items | Flags |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['stem']}` | {row['abstract_chars']} | {row['conclusion_chars']} | "
            f"{row['reference_count']} | {row['toc_count']} | {row['flags']} |"
        )

    lines.extend(["", "## Missing Reports", ""])
    lines.append("None." if not missing_reports else "\n".join(f"- `{item}`" for item in missing_reports))
    lines.extend(["", "## Missing Evidence", ""])
    lines.append("None." if not missing_evidence else "\n".join(f"- `{item}`" for item in missing_evidence))
    lines.extend(["", "## Report String Problems", ""])
    if report_problems:
        for stem, absent in report_problems:
            lines.append(f"- `{stem}`: {', '.join(absent)}")
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
