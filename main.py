# %% Cell 1 (Local Imports)
import csv
import logging
import time

# %% Cell 2 (Lib Imports)
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from config import CSV_DATA_FILENAME, HEADERS, MARKUP_FILENAME, URL
from utils.utils import data_handler

# %% Cell 3 (Functions and var declarations)
# NOTE: Writes the headers to the CSV file
with open(CSV_DATA_FILENAME, "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.DictWriter(f, fieldnames=HEADERS)

    csv_writer.writeheader()


# %% Cell 4
# Webdriver for chrome
browser = webdriver.Chrome()

# Maximazing allows the parser configurations to work more smoothly for avoiding 'no element exceptions'
browser.maximize_window()

# Opens the url using webdriver
browser.get(URL)

# Implicitly waiting for the page to load its contents in seconds
# Customize the time if your internet is slow
browser.implicitly_wait(40)

# page_element = browser.find_element(
#     By.XPATH, "(//span[@class='_18lf326a'])[1]")
page_element = browser.find_element(By.XPATH, "(//span[@class='_1xhlznaa'])[1]")

num_of_pages = (int(page_element.text) // 12) + 3  # Calculates the number of pages

# Handling var unbound
scroll_container = None
page = 0

try:
    # Accessing the scroll element in DOM to get the whole HTML markup so that beautifulSoup can parse it according to the headers list config
    try:
        scroll_container = browser.find_element(
            By.XPATH, "(//div[@class='_15gu4wr'])[3]"
        )
    except NoSuchElementException:
        scroll_container = browser.find_element(
            By.XPATH, "(//div[@class='_15gu4wr'])[2]"
        )
    finally:
        # Parses and navigates through all the pages
        for page in range(1, num_of_pages):
            with open(MARKUP_FILENAME, "w", encoding="utf-8") as f:
                f.write(browser.page_source)

            # Handles the parsing and writing of CSV data
            data_handler(page)

            time.sleep(2)
            # Scrolls the <ul></ul> element
            browser.execute_script(
                "arguments[0].scrollIntoView(false);", scroll_container
            )

            time.sleep(1)
            # Clicks on the next page <DOM element>
            browser.find_element(By.XPATH, "//div[@class='_5ocwns']//div[2]").click()

except (
    IndexError
):  # This error is triggered when the script crosses the page limit in the UI
    logging.debug(f"Total pages parsed {page - 1}")
    time.sleep(3)
finally:
    time.sleep(2)
    browser.quit()  # Exiting the Chrome driver
