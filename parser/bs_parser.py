import logging
import re

from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium.common.exceptions import NoSuchElementException

from utils import ColumnData, DataList, StrOrNull

_SELECTORS = {
    "result_card": "_1kf6gff",
    "type": "_oqoid",
    "title": "_1al0wlf",
    "rating": "_y10azs",
    "address_outer": "_14quei",
    "address_inner": "_1w9o2igt",
}


def extract_address_val(markup_content: str) -> StrOrNull:
    # Regex is used here because BS4 nested class matching is unreliable for this span structure
    sub_doc = BeautifulSoup(markup_content, "html.parser")
    addresses = [
        k for k in sub_doc.find_all("span", class_=_SELECTORS["address_outer"])
    ]

    if addresses:
        address_spans = re.findall(
            f'(<span class="{_SELECTORS["address_inner"]}">(.|\n)*?</span>)',
            str(addresses[0]),
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


def get_structured_data(
    html_content: str,
) -> ColumnData:
    doc = BeautifulSoup(html_content, features="html.parser")
    parent_div_results = doc.find_all("div", class_=_SELECTORS["result_card"])

    logging.debug(f"PARSER: {len(parent_div_results)} RESULT CARDS FOUND")

    TITLES: DataList = []
    TYPES: DataList = []
    ADDRESSES: DataList = []
    RATINGS: DataList = []

    for res_div in parent_div_results:
        type_tag: Tag | None = res_div.find("span", class_=_SELECTORS["type"])
        title_tag: Tag | None = res_div.find("span", class_=_SELECTORS["title"])
        rating_tag: Tag | None = res_div.find("div", class_=_SELECTORS["rating"])
        address = extract_address_val(
            str(res_div.find("span", class_=_SELECTORS["address_outer"]))
        )

        if (type_tag or title_tag or rating_tag) is None:
            raise NoSuchElementException(
                "Content Tag(s) are None. Try changing the class_"
            )
        else:
            type: StrOrNull = type_tag.text if type_tag is not None else "null"
            title: StrOrNull = title_tag.text if title_tag is not None else type
            rating: StrOrNull = rating_tag.text if rating_tag is not None else "null"

            TITLES.append(title)
            TYPES.append(type)
            ADDRESSES.append(address)
            RATINGS.append(rating)

    return ColumnData(TITLES, TYPES, ADDRESSES, RATINGS)
