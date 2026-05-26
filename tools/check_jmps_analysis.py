from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_HEADINGS = [
    "## 1. 基本信息",
    "## 2. 一句话主张",
    "## 3. 选题与问题意识",
    "## 4. 领域位置与 Gap",
    "## 5. 创新性判断",
    "## 6. 论证链条",
    "## 7. 方法与证据",
    "## 8. 结构布局",
    "## 9. 文笔画像",
    "## 10. 引用策略",
    "## 11. 审稿风险",
    "## 12. 可复用资产",
    "## 13. 总结",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Check JMPS analysis outputs.")
    parser.add_argument("--manifest", default="jmps/文本/_manifest.json")
    parser.add_argument("--analysis-dir", default="jmps/拆解/papers")
    parser.add_argument("--summary-dir", default="jmps/拆解/batch_summaries")
    parser.add_argument("--report", default="jmps/拆解/_quality_report.md")
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    analysis_dir = Path(args.analysis_dir)
    summary_dir = Path(args.summary_dir)

    rows = []
    missing = []
    short = []
    missing_headings = []

    for record in manifest:
        stem = record["stem"]
        path = analysis_dir / f"{stem}.md"
        if not path.exists():
            rows.append((stem, "missing", 0, len(REQUIRED_HEADINGS), ""))
            missing.append(stem)
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        absent = [heading for heading in REQUIRED_HEADINGS if heading not in text]
        status = "ok"
        if len(text) < 2500 and "Erratum" not in stem:
            status = "short"
            short.append(stem)
        if absent:
            status = "missing headings"
            missing_headings.append((stem, absent))
        rows.append((stem, status, len(text), len(absent), path.name))

    summaries = sorted(summary_dir.glob("batch_*.md"))

    lines = [
        "# JMPS Analysis Quality Report",
        "",
        f"Expected papers: {len(manifest)}",
        f"Analysis files: {len(list(analysis_dir.glob('*.md')))}",
        f"Batch summaries: {len(summaries)}",
        "",
        "## Paper Checks",
        "",
        "| Stem | Status | Chars | Missing headings | File |",
        "| --- | --- | ---: | ---: | --- |",
    ]
    for stem, status, chars, absent_count, file_name in rows:
        lines.append(f"| `{stem}` | {status} | {chars} | {absent_count} | {file_name} |")

    lines.extend(["", "## Missing Files", ""])
    lines.append("None." if not missing else "\n".join(f"- `{item}`" for item in missing))

    lines.extend(["", "## Short Non-Erratum Files", ""])
    lines.append("None." if not short else "\n".join(f"- `{item}`" for item in short))

    lines.extend(["", "## Missing Heading Details", ""])
    if not missing_headings:
        lines.append("None.")
    else:
        for stem, absent in missing_headings:
            lines.append(f"- `{stem}`: {', '.join(absent)}")

    Path(args.report).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.report}")
    print(f"missing={len(missing)} short={len(short)} missing_headings={len(missing_headings)}")


if __name__ == "__main__":
    main()
