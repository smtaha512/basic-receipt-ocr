from receipt_parsers import tedi_receipt_parser


def parse_receipt(text: list[str]) -> list[str]:
  return tedi_receipt_parser.parse_receipt(text)