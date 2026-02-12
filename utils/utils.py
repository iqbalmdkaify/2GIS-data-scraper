import csv
import logging
import re
from typing import Literal

from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium.common.exceptions import NoSuchElementException

from config import CSV_DATA_FILENAME, MARKUP_FILENAME


def extract_address(markup_text) -> str | Literal["null"]:
    """
    Extracts and returns the text content of the first address span element from the given HTML markup text.

    This function parses the input HTML markup to find a span element with the class "_14quei" which typically
    contains address information. It then uses a regular expression to locate a nested span with the class
    "_1w9o2igt" inside the address span and extracts its text content. If no such element is found, it returns "null".

    Args:
        markup_text (str): A string containing HTML markup from which to extract the address content.

    Returns:
        str: The extracted text content of the address if found, otherwise "null".
    """
    sub_doc = BeautifulSoup(markup_text, "html.parser")
    addresses = [k for k in sub_doc.find_all("span", class_="_14quei")]

    if addresses:
        address_spans = re.findall(
            '(<span class="_1w9o2igt">(.|\n)*?</span>)', str(addresses[0])
        )

        if address_spans:
            return BeautifulSoup(
                str(address_spans[0][0] if address_spans[0][0] else address_spans[0]),
                "html.parser",
            ).text
        else:
            return "null"
    else:
        return "null"


def data_handler(page_number: int) -> None:
    """
    Processes the HTML markup stored in a local file to extract relevant data such as titles, types, addresses, and ratings
    for a given page of search results. The extracted data is then appended to a CSV file for further use or analysis.

    Args:
        page_number (int): The current page number being processed, used for logging purposes.

    This function reads the HTML content from a predefined file, parses it to locate specific elements containing the desired
    information, and organizes this data into lists. It subsequently writes the collected data rows to a CSV file and logs
    the completion of parsing for the given page.
    """
    with open(MARKUP_FILENAME, "r", encoding="utf-8") as f:
        contents = f.read()

    # NOTE: The <doc> variable holds the markup data read from the HTML file
    doc = BeautifulSoup(contents, features="html.parser")

    parent_div_results = doc.find_all("div", class_="_1kf6gff")

    TITLES: list[str | Literal["null"]] = []
    TYPES: list[str | Literal["null"]] = []
    ADDRESSES: list[str | Literal["null"]] = []
    RATINGS: list[str | Literal["null"]] = []

    for idx, res_div in enumerate(parent_div_results):
        type_tag: Tag | None = res_div.find("span", class_="_oqoid")
        title_tag: Tag | None = res_div.find("span", class_="_1al0wlf")
        rating_tag: Tag | None = res_div.find("div", class_="_y10azs")
        address = extract_address(str(res_div.find("span", class_="_14quei")))

        if (type_tag or title_tag or rating_tag) is None:
            raise NoSuchElementException(
                "Content Tag(s) are None. Try changing the class_"
            )
        else:
            type: str | Literal["null"] = (
                type_tag.text if type_tag is not None else "null"
            )

            title: str | Literal["null"] = (
                title_tag.text if title_tag is not None else type
            )

            rating: str | Literal["null"] = (
                rating_tag.text if rating_tag is not None else "null"
            )

            # Appending each page data to their corresponding lists
            TITLES.append(title)
            TYPES.append(type)
            ADDRESSES.append(address)
            RATINGS.append(rating)

    # Writes row data for current page
    with open(CSV_DATA_FILENAME, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        for m in range(1, len(TITLES)):
            writer.writerow([TITLES[m], TYPES[m], ADDRESSES[m], RATINGS[m]])

    logging.info(f"Finished parsing page: {page_number}")  # Logger for parsing status
