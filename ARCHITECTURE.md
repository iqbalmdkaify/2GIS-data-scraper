# Architecture Overview

## High-level flow

```
CLI args
   │
   ▼
main.py  ──►  Runner
                │
                ├──► Executor        (browser session + navigation)
                │       │
                │       └── page_source (HTML string)
                │
                ├──► Parser          (HTML → ColumnData)
                │
                └──► IO Handler      (ColumnData → CSV)
```

1. `main.py` parses CLI arguments, initialises the logger, and hands control to `Runner`.
2. `Runner` calls `Executor` to open a Chrome session and navigate to the search URL.
3. For each page, `Runner` reads `driver.page_source` and passes it to `Parser`.
4. `Parser` extracts structured data and returns a `ColumnData` object.
5. `Runner` passes `ColumnData` to `IO Handler`, which appends a row to the output CSV.
6. `Runner` instructs `Executor` to scroll and click to the next page, then repeats from step 3.

---

## Layer responsibilities

### `executor/`
Owns all Selenium interactions. No business logic lives here — only browser primitives.

- `create_session` / `quit_session` — Chrome WebDriver lifecycle
- `navigate`, `find`, `click_element`, `scroll_into_view`, `wait` — browser actions
- `XPATHS` — all DOM locators in one place; update here when the 2GIS UI changes

### `parser/`
Pure transformation layer. Receives an HTML string, returns structured data. No I/O, no Selenium.

- `get_structured_data(html_content)` → `ColumnData`
- `extract_address_val` — isolates the nested address span using regex; BS4 nested class matching is unreliable for this element
- `_SELECTORS` — all CSS class names in one place; update here when the 2GIS markup changes

### `io_handler/`
Owns all file system writes.

- `write_csv_headers` — initialises the output CSV with column names
- `write_to_csv` — appends one page of results
- `write_to_file` — writes raw page source to disk for debugging

### `runner/`
Orchestrator. Calls the three layers above in the correct order. Contains pagination logic and error handling, but no parsing, no direct Selenium calls, no file I/O of its own.

### `utils/`
Shared infrastructure with no layer affiliation.

- `cli_parser` — argument definitions (`city_name`, `query_string`, `-o`, `-l`)
- `loggers` — `basicConfig` wrapper; log level accepted as a CLI flag
- `types` — `ColumnData`, `DataList`, `StrOrNull` type aliases
- `utils` — `build_search_query` URL builder

---

## Data types

```
StrOrNull   = str | Literal["null"]
DataList    = List[StrOrNull]

ColumnData:
    title:   DataList
    type:    DataList
    address: DataList
    rating:  DataList
```

---

## Repository layout

```
2GIS-data-scraper/
├── main.py                  # Entry point
├── executor/
│   ├── executor.py          # Selenium primitives + XPATHS
│   └── __init__.py
├── parser/
│   ├── bs_parser.py         # BeautifulSoup parsing + _SELECTORS
│   └── __init__.py
├── io_handler/
│   ├── handler.py           # CSV + file writes
│   └── __init__.py
├── runner/
│   ├── runner.py            # Orchestration + pagination loop
│   └── __init__.py
├── utils/
│   ├── cli_parser.py
│   ├── loggers.py
│   ├── types.py
│   ├── utils.py
│   └── __init__.py
├── data/
│   ├── raw.csv              # Scrape output (default path)
│   └── temp.txt             # Debug page-source snapshot (overwritten each page)
├── pyproject.toml
└── README.md
```

---

## Selector maintenance

Two dictionaries own all target-site selectors. When the 2GIS UI changes class names or DOM structure, these are the only files that need updating:

| Dictionary | File | Used by |
|---|---|---|
| `_SELECTORS` | `parser/bs_parser.py` | BeautifulSoup (CSS classes) |
| `XPATHS` | `executor/executor.py` | Selenium (DOM locators) |
