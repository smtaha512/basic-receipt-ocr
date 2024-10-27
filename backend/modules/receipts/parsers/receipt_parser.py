from . import e_center_receipt_parser, tedi_receipt_parser
from .exceptions.parser_not_found_exception import ParserNotFoundException
from .utils.fuzzy_match import fuzzy_match

EXPECTED_STORES = ["TEDI", "E-Center", "TEDI GmbH & Co"]


def parse_receipt(text: list[str]) -> str:  # ParsedReceipt | str:
    # First item contains receipt content in a string. Each item in the string is separated by a new line
    receipt_content: list[str] = next(map(lambda text: text.description, text)).split(
        "\n"
    )

    store_name = next(
        map(lambda item: fuzzy_match(item, EXPECTED_STORES), receipt_content)
    )

    if store_name.startswith("E-Center"):
        return e_center_receipt_parser.parse_receipt(receipt_content)
    elif store_name.startswith("TEDI") or store_name.startswith("TEDI GmbH & Co"):
        return tedi_receipt_parser.parse_receipt(receipt_content)
    else:
        raise ParserNotFoundException(store_name)
