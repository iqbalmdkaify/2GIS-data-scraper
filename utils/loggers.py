import argparse
import logging


def parse_log_level(value: str) -> logging._Level:
    log_value = value.upper()

    if log_value not in logging._nameToLevel:
        raise argparse.ArgumentTypeError(
            f"Invalid logging level {value}. Choose from {list(logging._nameToLevel.keys())}"
        )
    else:
        return logging._nameToLevel[log_value]


def initiate_logger(level: logging._Level) -> None:
    logging.basicConfig(
        level=level, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
