import itertools
from typing import List

def parse_receipt_from_tedi(texts: List[str]) -> List[str]:
  return list(itertools.chain.from_iterable(map(lambda text: text.description.split("\n"), texts)))[5:8]