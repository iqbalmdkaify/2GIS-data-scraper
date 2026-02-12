# Logging config
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Headers for CSV file
HEADERS = ["title", "type", "address", "rating"]  # default

MARKUP_FILENAME: str = "html-markup.txt"
CSV_DATA_FILENAME: str = "data.csv"

# NOTE: Set the city name, search to your own for which you want to get the data. Below mentioned is an example
CITY_NAME: str = "Moscow"
SEARCH: str = "University"

URL = f"https://2gis.ru/{CITY_NAME.lower()}/search/{SEARCH.title()}?m"
# URL = 'https://2gis.ru/kazan/search/%D0%B6%D0%BA?m=49.255846%2C55.793323%2F10.89'
