import argparse
import sys
from pathlib import Path

import markdown
from weasyprint import HTML


def convert(input_path: Path, output_path: Path) -> None:
    md_text = input_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "toc", "sane_lists"],
    )
    html_doc = (
        "<!DOCTYPE html><html><head>"
        f"<meta charset='utf-8'><title>{input_path.stem}</title>"
        "</head><body>"
        f"{html_body}"
        "</body></html>"
    )
    HTML(string=html_doc, base_url=str(input_path.parent)).write_pdf(str(output_path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a Markdown file to PDF.")
    parser.add_argument("input", type=Path, help="Path to the input .md file")
    parser.add_argument("output", type=Path, help="Path to the output .pdf file")
    args = parser.parse_args()

    if not args.input.is_file():
        sys.exit(f"Input file not found: {args.input}")

    convert(args.input, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
