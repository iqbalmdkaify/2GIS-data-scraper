import argparse
import logging

from .loggers import parse_log_level

cli_parser = argparse.ArgumentParser(
    prog="2GIS Data Scrapper",
    description="This program extracts data from 2GIS Map",
    exit_on_error=True,
)

# Positional Arguments
cli_parser.add_argument("city_name", type=str)
cli_parser.add_argument("query_string", type=str)

# Optional Arguments
cli_parser.add_argument(
    "-o",
    "--output_path",
    type=str,
    default="./data/raw.csv",
    help="Supports only .csv format",
)

cli_parser.add_argument(
    "-l",
    "--log",
    type=parse_log_level,
    help="Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    default=logging.INFO,
)


def initiate_cli_parser() -> argparse.Namespace:
    return cli_parser.parse_args()
