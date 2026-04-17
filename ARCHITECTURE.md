# Architecture Overview

## High-level flow
1. `main.ipynb` builds a 2GIS search URL using `CITY_NAME` and `SEARCH`.
2. Selenium opens the 2GIS UI and paginates through results.
3. For each page, the notebook writes the current `browser.page_source` to `html-markup.txt`.
4. `data_handler()` reads `html-markup.txt`, parses it with BeautifulSoup, and appends rows to `data.csv`.
5. The final notebook cell optionally de-duplicates `data.csv` with pandas.

## Repository layout
- `main.ipynb`: Single-notebook implementation of the scraper. Defines constants, parsing helpers, Selenium navigation, pagination logic, and optional de-duplication of the CSV output.
- `requirements.txt`: Pinned Python dependencies required to run the notebook (selenium, beautifulsoup4, pandas, and Jupyter-related packages).
- `html-markup.txt`: Sample/temporary HTML snapshot captured from the 2GIS UI. The notebook overwrites this file each page to provide input for BeautifulSoup parsing.
- `data.csv`: Sample output file containing scraped results. The notebook writes and appends rows to this file during execution.
- `images/`: Documentation assets referenced from the README.
  - `capture_20231115154824785.bmp`: Screenshot of the required import section in the notebook.
  - `capture_20231115154838058.bmp`: Screenshot of mandatory code blocks in the notebook.
  - `readme.txt`: Short note describing the purpose of the images folder.
- `README.md`: Project description, setup steps, and usage instructions.
- `LICENSE.md`: Apache 2.0 license text.
- `.gitignore`: Ignores local virtual environment folders and configuration artifacts.
