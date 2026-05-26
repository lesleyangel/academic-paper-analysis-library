from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines).strip()


def extract_pdf(pdf_path: Path, text_dir: Path, meta_dir: Path) -> dict[str, Any]:
    doc = fitz.open(pdf_path)
    metadata = dict(doc.metadata or {})
    toc = doc.get_toc(simple=True)

    page_records: list[dict[str, Any]] = []
    text_parts: list[str] = []

    for page_index, page in enumerate(doc, start=1):
        raw_text = page.get_text("text", sort=True)
        text = normalize_text(raw_text)
        page_records.append(
            {
                "page": page_index,
                "chars": len(text),
                "words_estimate": len(text.split()),
            }
        )
        text_parts.append(
            f"\n\n===== PAGE {page_index} / {doc.page_count} =====\n\n{text}\n"
        )

    full_text = normalize_text("".join(text_parts))
    text_path = text_dir / f"{pdf_path.stem}.txt"
    meta_path = meta_dir / f"{pdf_path.stem}.json"

    text_header = "\n".join(
        [
            f"# Source PDF: {pdf_path.name}",
            f"# Extracted at: {datetime.now().isoformat(timespec='seconds')}",
            f"# Extraction method: PyMuPDF get_text('text', sort=True)",
            f"# Pages: {doc.page_count}",
            f"# PDF SHA256: {file_sha256(pdf_path)}",
            "",
        ]
    )
    text_path.write_text(text_header + full_text + "\n", encoding="utf-8")

    record: dict[str, Any] = {
        "pdf": str(pdf_path),
        "pdf_name": pdf_path.name,
        "stem": pdf_path.stem,
        "text_file": str(text_path),
        "metadata_file": str(meta_path),
        "title": metadata.get("title") or "",
        "author": metadata.get("author") or "",
        "subject": metadata.get("subject") or "",
        "keywords": metadata.get("keywords") or "",
        "creator": metadata.get("creator") or "",
        "producer": metadata.get("producer") or "",
        "page_count": doc.page_count,
        "text_chars": len(full_text),
        "text_words_estimate": len(full_text.split()),
        "pages": page_records,
        "toc": [
            {"level": item[0], "title": item[1], "page": item[2]} for item in toc
        ],
        "pdf_sha256": file_sha256(pdf_path),
        "extraction_method": "pymupdf_text_sort_true",
        "extracted_at": datetime.now().isoformat(timespec="seconds"),
    }

    meta_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    doc.close()
    return record


def write_reports(records: list[dict[str, Any]], out_dir: Path) -> None:
    manifest_path = out_dir / "_manifest.json"
    manifest_path.write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    report_lines = [
        "# JMPS PDF Text Extraction Report",
        "",
        f"Generated at: {datetime.now().isoformat(timespec='seconds')}",
        f"PDF count: {len(records)}",
        "",
        "| # | PDF | Pages | Chars | Words est. | Text file |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for idx, record in enumerate(records, start=1):
        report_lines.append(
            "| {idx} | {pdf} | {pages} | {chars} | {words} | {text_file} |".format(
                idx=idx,
                pdf=record["pdf_name"].replace("|", "\\|"),
                pages=record["page_count"],
                chars=record["text_chars"],
                words=record["text_words_estimate"],
                text_file=Path(record["text_file"]).name,
            )
        )

    report_lines.extend(
        [
            "",
            "## Low-Text Warnings",
            "",
        ]
    )
    warnings = [
        record
        for record in records
        if record["text_chars"] < max(2000, record["page_count"] * 300)
    ]
    if not warnings:
        report_lines.append("No low-text warnings.")
    else:
        for record in warnings:
            report_lines.append(
                f"- {record['pdf_name']}: {record['text_chars']} chars across {record['page_count']} pages"
            )

    (out_dir / "_extraction_report.md").write_text(
        "\n".join(report_lines) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract readable text from all JMPS PDFs."
    )
    parser.add_argument(
        "--pdf-dir",
        default="jmps/文献",
        help="Directory containing PDF files.",
    )
    parser.add_argument(
        "--out-dir",
        default="jmps/文本",
        help="Output directory for extracted text and metadata.",
    )
    args = parser.parse_args()

    pdf_dir = Path(args.pdf_dir)
    out_dir = Path(args.out_dir)
    text_dir = out_dir / "txt"
    meta_dir = out_dir / "metadata"
    text_dir.mkdir(parents=True, exist_ok=True)
    meta_dir.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {pdf_dir}")

    records: list[dict[str, Any]] = []
    for pdf_path in pdfs:
        print(f"Extracting {pdf_path.name}")
        try:
            records.append(extract_pdf(pdf_path, text_dir, meta_dir))
        except Exception as exc:  # Keep the batch moving and report failures.
            records.append(
                {
                    "pdf": str(pdf_path),
                    "pdf_name": pdf_path.name,
                    "stem": pdf_path.stem,
                    "error": repr(exc),
                    "extracted_at": datetime.now().isoformat(timespec="seconds"),
                }
            )

    write_reports(records, out_dir)
    failures = [record for record in records if "error" in record]
    print(f"Done. PDFs: {len(records)}. Failures: {len(failures)}.")
    if failures:
        for failure in failures:
            print(f"FAILED {failure['pdf_name']}: {failure['error']}")


if __name__ == "__main__":
    main()
