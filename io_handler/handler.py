import csv
import logging

from utils import ColumnData

HEADERS = ["title", "type", "address", "rating"]


def write_csv_headers(file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=HEADERS)
        csv_writer.writeheader()


def write_to_csv(page_number: int, data: ColumnData, file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        for m in range(1, len(data.title)):
            writer.writerow(
                [data.title[m], data.type[m], data.address[m], data.rating[m]]
            )

    logging.info(f"PAGE {page_number} WRITTEN TO CSV")


def write_to_file(file_path: str, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as writable_file:
        writable_file.write(content)
