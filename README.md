# pdf_creator

CLI що конвертує Markdown-файл у PDF. Парсить MD через пакет `markdown`
(розширення: `fenced_code`, `tables`, `toc`, `sane_lists`), обгортає у
мінімальний HTML і рендерить у PDF за допомогою WeasyPrint. Батьківська
директорія MD-файлу передається як `base_url`, тож відносні посилання на
зображення та інші ресурси резолвляться коректно.

## Стек

- Менеджер пакетів/середовища: [uv](https://github.com/astral-sh/uv)
- Python: 3.14
- Залежності: `markdown`, `weasyprint`

## Системна залежність: Pango

WeasyPrint підвантажує Pango/Cairo через FFI під час імпорту. На macOS:

```sh
brew install pango
```

Без цього навіть `from weasyprint import HTML` падає з
`OSError: cannot load library 'libpango-1.0-0'`.

## Використання

```sh
uv sync
uv run main.py <input.md> <output.pdf>
```
