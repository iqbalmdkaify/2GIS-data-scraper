# 2GIS Data Scraper

Scrapes business listings from [2GIS](https://2gis.ru) by city and search query. Uses Selenium to drive Chrome through paginated search results and BeautifulSoup to extract structured data, outputting to CSV.

Extracted fields: `title`, `type`, `address`, `rating`.

---

## Requirements

- Python 3.11
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Google Chrome (latest)

ChromeDriver is managed automatically by Selenium — no manual download required.

---

## Setup

```bash
git clone https://github.com/iqbalmdkaify/2GIS-data-scraper.git
cd 2GIS-data-scraper

uv venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

uv pip install selenium beautifulsoup4
```

---

## Usage

```
python main.py <city_name> <query_string> [options]
```

### Arguments

| Argument | Type | Description |
|---|---|---|
| `city_name` | positional | City to search in (e.g. `moscow`) |
| `query_string` | positional | Search term (e.g. `coffee`) |
| `-o`, `--output_path` | optional | Output CSV path. Default: `./data/raw.csv` |
| `-l`, `--log` | optional | Log level: `DEBUG`, `INFO`, `WARNING`, `ERROR`. Default: `INFO` |

### Examples

```bash
# Basic
python main.py moscow coffee

# Custom output path
python main.py novosibirsk hotel -o ./data/hotels.csv

# With debug logging
python main.py almaty restaurant -l DEBUG
```

---

## Output

Results are written to `./data/raw.csv` (or the path set via `-o`). A raw HTML snapshot of each page is saved to `../data/temp.txt` during the run for debugging.

Example output:

| title | type | address | rating |
|---|---|---|---|
| Shokolad | Cafe | ul. Lenina 12 | 4.7 |
| Coffee House | Coffee shop | pr. Mira 5 | 4.3 |

---

## License

[Apache License 2.0](LICENSE.md)
