from typing import Callable


def get_parser_by_marketplace_code(marketplace_code: str) -> Callable:
    parsers = {
        "sreality": parser_sreality,
    }

    return parsers[marketplace_code]


def parser_sreality(source_link):
    return 5
