from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


SKILL_SCRIPT = Path(r"C:\Users\90793\.codex\skills\academic-pdf-cleantext\scripts\extract_academic_pdf.py")


def slugify(path: Path, index: int) -> str:
    stem = path.stem
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem)
    stem = re.sub(r"-{2,}", "-", stem).strip("-._")
    if len(stem) > 120:
        stem = stem[:120].rstrip("-._")
    return f"{index:03d}-{stem or 'paper'}"


def has_success(out_dir: Path) -> bool:
    report_path = out_dir / "extraction_report.json"
    clean_body = out_dir / "clean_body.txt"
    if not report_path.exists() or not clean_body.exists():
        return False
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception:
        return False
    return clean_body.stat().st_size > 100 and bool(report.get("body_chars", 0))


def load_report(out_dir: Path) -> dict:
    report_path = out_dir / "extraction_report.json"
    if not report_path.exists():
        return {}
    try:
        return json.loads(report_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"report_error": str(exc)}


def run_one(pdf: Path, out_dir: Path, args: argparse.Namespace) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "extraction.log"
    command = [
        sys.executable,
        str(SKILL_SCRIPT),
        str(pdf),
        "--out",
        str(out_dir),
        "--mineru-backend",
        args.mineru_backend,
        "--mineru-model-source",
        args.mineru_model_source,
    ]
    if args.no_mineru:
        command.append("--no-mineru")
    if args.no_docling:
        command.append("--no-docling")
    if args.no_marker:
        command.append("--no-marker")
    if args.grobid_url:
        command.extend(["--grobid-url", args.grobid_url])

    started = time.time()
    completed = subprocess.run(command, capture_output=True, text=True, timeout=args.timeout)
    elapsed = round(time.time() - started, 2)
    log = {
        "pdf": str(pdf),
        "out_dir": str(out_dir),
        "command": command,
        "returncode": completed.returncode,
        "elapsed_seconds": elapsed,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "finished_at": datetime.now().isoformat(timespec="seconds"),
    }
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if completed.returncode != 0:
        return {
            "pdf": str(pdf),
            "out_dir": str(out_dir),
            "status": "failed",
            "elapsed_seconds": elapsed,
            "error": (completed.stderr or completed.stdout)[-2000:],
        }

    report = load_report(out_dir)
    return summarize(pdf, out_dir, "ok", elapsed, report)


def summarize(pdf: Path, out_dir: Path, status: str, elapsed: float | None, report: dict) -> dict:
    audit = report.get("audit", {}) if isinstance(report, dict) else {}
    formula_audit = audit.get("formula_audit", {}) if isinstance(audit, dict) else {}
    return {
        "pdf": str(pdf),
        "paper_id": out_dir.name,
        "out_dir": str(out_dir),
        "status": status,
        "elapsed_seconds": elapsed,
        "body_chars": report.get("body_chars", 0),
        "references_count": report.get("references_count", 0),
        "tables_count": report.get("tables_count", 0),
        "figure_captions_count": report.get("figure_captions_count", 0),
        "equations_count": report.get("equations_count", 0),
        "noise_flags": report.get("noise_flags", []),
        "audit_score": audit.get("quality_score"),
        "needs_manual_review": audit.get("needs_manual_review"),
        "issues_after_repair": audit.get("issues_after_repair", []),
        "chosen_sources": report.get("chosen_sources", {}),
        "formula_low_confidence_count": formula_audit.get("low_confidence_count"),
    }


def write_summary(summary_path: Path, rows: list[dict]) -> None:
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = [
        "# 801 academic-pdf-cleantext batch summary",
        "",
        f"- total: {len(rows)}",
        f"- ok: {sum(1 for row in rows if row['status'] in {'ok', 'skipped'})}",
        f"- failed: {sum(1 for row in rows if row['status'] == 'failed')}",
        f"- needs_manual_review: {sum(1 for row in rows if row.get('needs_manual_review'))}",
        "",
        "| # | status | body chars | refs | tables | equations | audit | review | paper |",
        "|---:|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for idx, row in enumerate(rows, start=1):
        md.append(
            "| {idx} | {status} | {body} | {refs} | {tables} | {eqs} | {audit} | {review} | {paper} |".format(
                idx=idx,
                status=row.get("status", ""),
                body=row.get("body_chars", 0),
                refs=row.get("references_count", 0),
                tables=row.get("tables_count", 0),
                eqs=row.get("equations_count", 0),
                audit="" if row.get("audit_score") is None else row.get("audit_score"),
                review="yes" if row.get("needs_manual_review") else "",
                paper=Path(row.get("pdf", "")).name.replace("|", "\\|"),
            )
        )
    summary_path.with_suffix(".md").write_text("\n".join(md) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Batch extract 801 PDFs with academic-pdf-cleantext.")
    parser.add_argument("--pdf-dir", default=r"F:\code\学术期刊蒸馏器\801\论文")
    parser.add_argument("--out-root", default=r"F:\code\学术期刊蒸馏器\801\cleantext")
    parser.add_argument("--summary", default=r"F:\code\学术期刊蒸馏器\801\cleantext\batch_summary.json")
    parser.add_argument("--start", type=int, default=0, help="Zero-based start index in sorted PDF list.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of PDFs to process. 0 means all remaining.")
    parser.add_argument("--force", action="store_true", help="Re-run even when extraction_report.json already exists.")
    parser.add_argument("--timeout", type=int, default=1200, help="Per-paper timeout in seconds.")
    parser.add_argument("--mineru-backend", default="pipeline")
    parser.add_argument("--mineru-model-source", default=os.environ.get("MINERU_MODEL_SOURCE", "modelscope"))
    parser.add_argument("--grobid-url", default="")
    parser.add_argument("--no-mineru", action="store_true")
    parser.add_argument("--no-docling", action="store_true")
    parser.add_argument("--no-marker", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf_dir = Path(args.pdf_dir)
    out_root = Path(args.out_root)
    pdfs = sorted(pdf_dir.glob("*.pdf"), key=lambda p: p.name.lower())
    selected = pdfs[args.start :]
    if args.limit > 0:
        selected = selected[: args.limit]
    out_root.mkdir(parents=True, exist_ok=True)

    existing_rows: list[dict] = []
    summary_path = Path(args.summary)
    if summary_path.exists():
        try:
            existing_rows = json.loads(summary_path.read_text(encoding="utf-8"))
        except Exception:
            existing_rows = []
    by_pdf = {row.get("pdf"): row for row in existing_rows}

    rows = existing_rows[:]
    print(f"Found {len(pdfs)} PDFs; selected {len(selected)}; output={out_root}", flush=True)
    for pdf in selected:
        index = pdfs.index(pdf) + 1
        out_dir = out_root / slugify(pdf, index)
        print(f"[{index}/{len(pdfs)}] {pdf.name}", flush=True)
        if not args.force and has_success(out_dir):
            report = load_report(out_dir)
            row = summarize(pdf, out_dir, "skipped", None, report)
            print(
                f"  skipped body={row['body_chars']} refs={row['references_count']} audit={row['audit_score']}",
                flush=True,
            )
        else:
            try:
                row = run_one(pdf, out_dir, args)
            except subprocess.TimeoutExpired as exc:
                row = {
                    "pdf": str(pdf),
                    "paper_id": out_dir.name,
                    "out_dir": str(out_dir),
                    "status": "failed",
                    "elapsed_seconds": args.timeout,
                    "error": f"timeout after {args.timeout}s: {exc}",
                }
                (out_dir / "extraction.log").write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            except Exception as exc:  # noqa: BLE001
                row = {
                    "pdf": str(pdf),
                    "paper_id": out_dir.name,
                    "out_dir": str(out_dir),
                    "status": "failed",
                    "elapsed_seconds": None,
                    "error": str(exc),
                }
                out_dir.mkdir(parents=True, exist_ok=True)
                (out_dir / "extraction.log").write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(
                f"  {row['status']} elapsed={row.get('elapsed_seconds')} body={row.get('body_chars', 0)} refs={row.get('references_count', 0)} audit={row.get('audit_score')}",
                flush=True,
            )
        by_pdf[str(pdf)] = row
        rows = [by_pdf.get(str(item), {}) for item in pdfs if by_pdf.get(str(item))]
        write_summary(summary_path, rows)

    write_summary(summary_path, rows)
    failed = sum(1 for row in rows if row.get("status") == "failed")
    print(f"Done. rows={len(rows)} failed={failed} summary={summary_path}", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
