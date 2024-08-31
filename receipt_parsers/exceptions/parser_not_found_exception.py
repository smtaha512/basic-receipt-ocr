class ParserNotFoundException(Exception):
  def __init__(self, store_name: str) -> None:
    super().__init__("Can not find parser for: " + store_name)