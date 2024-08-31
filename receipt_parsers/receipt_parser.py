from receipt_parsers import e_center_receipt_parser, tedi_receipt_parser
from receipt_parsers.exceptions.parser_not_found_exception import ParserNotFoundException
from receipt_parsers.types.parsed_receipt_type import ParsedReceipt


def parse_receipt(text: list[str]) -> ParsedReceipt:
  # First item contains receipt content in a string. Each item in the string is separated by a new line
  receipt_content: list[str] = next(map(lambda text: text.description, text)).split("\n")

  store_name = receipt_content[0]
  
  if(store_name.startswith("E-Center")):
    return e_center_receipt_parser.parse_receipt(receipt_content)
  elif(store_name.startswith("TEDI")):
    return tedi_receipt_parser.parse_receipt(receipt_content)
  else:
    raise ParserNotFoundException(store_name)
    