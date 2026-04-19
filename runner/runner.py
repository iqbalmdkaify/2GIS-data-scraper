import logging
import time
from argparse import Namespace

from executor import (
    XPATHS,
    click_element,
    create_session,
    find,
    navigate,
    quit_session,
    scroll_into_view,
    wait,
)
from executor.executor import NoSuchElement
from io_handler import write_csv_headers, write_to_csv
from io_handler.handler import write_to_file
from parser.bs_parser import get_structured_data
from utils import build_search_query


class Runner:
    def __init__(self, config: Namespace) -> None:
        self.search_query: str = build_search_query(
            city_name=config.city_name, query=config.query_string
        )
        self.output_dir: str = config.output_path
        self.markup_path: str = "../data/temp.txt"

    def run(self) -> None:
        write_csv_headers(self.output_dir)

        driver = create_session()
        navigate(driver=driver, url=self.search_query)

        # 40s gives slow connections enough time; lower if your network is fast
        wait(driver=driver, time=40)

        page_count_element = find(driver, XPATHS["result_count"])
        num_of_pages = (int(page_count_element.text) // 12) + 3

        logging.info(f"TOTAL PAGES TO SCRAPE: {num_of_pages - 2}")

        # Both must be bound before the try block to remain accessible in except/finally
        scroll_container = None
        page = 0

        try:
            try:
                scroll_container = find(driver, XPATHS["scroll_container_primary"])
            except NoSuchElement:
                scroll_container = find(driver, XPATHS["scroll_container_fallback"])

            for page in range(1, num_of_pages):
                # Snapshot saved for debugging only — not used by the parser
                write_to_file(file_path=self.markup_path, content=driver.page_source)

                col_data = get_structured_data(driver.page_source)
                write_to_csv(page_number=page, data=col_data, file_path=self.output_dir)

                time.sleep(2)
                scroll_into_view(driver, scroll_container)

                time.sleep(1)
                clickable_el = find(driver, XPATHS["next_page_btn"])
                click_element(clickable_el)

        except IndexError:
            # IndexError fires when the UI page count diverges from num_of_pages
            logging.info(f"SCRAPE COMPLETE — {page - 1} PAGES PROCESSED")
            time.sleep(3)
        finally:
            time.sleep(2)
            quit_session(driver)
