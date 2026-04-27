# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

CLI that converts a Markdown file to PDF. `main.py` parses MD via the `markdown` package (extensions: `fenced_code`, `tables`, `toc`, `sane_lists`), wraps it in a minimal HTML document, and renders to PDF with WeasyPrint. The MD file's parent directory is passed as `base_url` so relative image/asset references resolve.

## Toolchain

- Package/env manager: **uv** (see `uv.lock`)
- Python: **3.14** (pinned in `.python-version` and `pyproject.toml`'s `requires-python`)
- Runtime deps: `markdown`, `weasyprint`

## System dependency: Pango

WeasyPrint loads Pango/Cairo via FFI at import time. On macOS install with `brew install pango` — without it, even `from weasyprint import HTML` raises `OSError: cannot load library 'libpango-1.0-0'`. If you see that error, the fix is the brew install, not a Python-side change.

## Commands

- Convert a file: `uv run main.py <input.md> <output.pdf>`
- Add a dependency: `uv add <package>`
- Sync the venv from the lockfile: `uv sync`

No lint, format, or test tooling is configured yet — add it via `uv add --dev ...` when introducing the first such workflow rather than assuming a specific tool.
