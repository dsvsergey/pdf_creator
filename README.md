# pdf_creator

A CLI that converts a Markdown file to PDF. It parses MD via the
`markdown` package (extensions: `fenced_code`, `tables`, `toc`,
`sane_lists`), wraps it in a minimal HTML document, and renders it to
PDF with WeasyPrint. The MD file's parent directory is passed as
`base_url`, so relative references to images and other assets resolve
correctly.

## Stack

- Package/environment manager: [uv](https://github.com/astral-sh/uv)
- Python: 3.14
- Dependencies: `markdown`, `weasyprint`

## System dependency: Pango

WeasyPrint loads Pango/Cairo via FFI at import time. On macOS:

```sh
brew install pango
```

Without it, even `from weasyprint import HTML` fails with
`OSError: cannot load library 'libpango-1.0-0'`.

## Usage

```sh
uv sync
uv run main.py <input.md> <output.pdf>
```
