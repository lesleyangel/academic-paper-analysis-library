from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_HEADINGS = [
    "## 0. 读取说明",
    "## 1. 基本信息与论文身份",
    "## 2. 摘要与核心信息提取",
    "## 3. 选题层深拆",
    "## 4. 领域位置与文献版图",
    "## 5. Gap 制造机制",
    "## 6. 创新性判断",
    "## 7. 论证链条复原",
    "## 8. 方法/理论/模型细拆",
    "## 9. 证据系统与 Claim-Evidence 表",
    "## 10. 图表、公式与结果叙事提取",
    "## 11. 章节结构与篇章布局",
    "## 12. 段落功能与叙事节奏",
    "## 13. 文笔画像与语言习惯",
    "## 14. 常用词、句式与可复用表达提取",
    "## 15. 引用策略与文献使用",
    "## 16. 审稿人视角风险",
    "## 17. 可复用资产",
    "## 18. 对我写论文的启发",
    "## 19. 最终浓缩",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Check JMPS deep analysis outputs.")
    parser.add_argument("--manifest", default="jmps/文本/_manifest.json")
    parser.add_argument("--analysis-dir", default="jmps/深度拆解/papers")
    parser.add_argument("--summary-dir", default="jmps/深度拆解/batch_summaries")
    parser.add_argument("--report", default="jmps/深度拆解/_quality_report.md")
    parser.add_argument("--min-chars", type=int, default=10000)
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
            missing.append(stem)
            rows.append((stem, "missing", 0, len(REQUIRED_HEADINGS), path.name))
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        absent = [heading for heading in REQUIRED_HEADINGS if heading not in text]
        is_erratum = "Erratum" in stem or record.get("page_count") == 1

        status = "ok"
        if len(text) < args.min_chars and not is_erratum:
            status = "short"
            short.append(stem)
        if absent:
            status = "missing headings"
            missing_headings.append((stem, absent))

        rows.append((stem, status, len(text), len(absent), path.name))

    summaries = sorted(summary_dir.glob("batch_*.md"))
    lines = [
        "# JMPS Deep Analysis Quality Report",
        "",
        f"Expected papers: {len(manifest)}",
        f"Deep analysis files: {len(list(analysis_dir.glob('*.md')))}",
        f"Batch summaries: {len(summaries)}",
        f"Minimum chars for non-erratum: {args.min_chars}",
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
    print(
        "missing={missing} short={short} missing_headings={missing_headings}".format(
            missing=len(missing),
            short=len(short),
            missing_headings=len(missing_headings),
        )
    )


if __name__ == "__main__":
    main()
