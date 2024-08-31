from datetime import datetime,_Date
import re
from typing import Literal, TypedDict

Item = TypedDict('Item', serial_no=str, name=str, price=float)

ParsedReceipt = TypedDict("ParsedReceipt",
  items=list[Item],
  date=_Date,
  store_name=Literal['Tedi'],
)

def chunks(items: list[str], chunk_size: int):
  for i in range(0, len(items), chunk_size):
    yield items[i:i + chunk_size]

def parse_receipt(texts: list[str]) -> ParsedReceipt:
  receipt_content = list(map(lambda text: text.description, texts))[0].split("\n")
  
  index_of_first_item = 5
  index_of_last_item_price = receipt_content.index("Kaufsumme:") - 1
  
  items = receipt_content[index_of_first_item : index_of_last_item_price + 1]
  item_rows = list(chunks(items, 3))
  list_of_mapped_items: list[Item] = list(map(lambda item: { "serial_no": item[0], "name": item[1], "price": float(item[2]) }, item_rows))
  
  transaction_end_at: str = [item for _, item in enumerate(receipt_content) if re.search('\d{4}-\d{2}-\d{2}T\d{2}', item)][1:2][0]
  
  parsed_receipt: ParsedReceipt = { "items": list_of_mapped_items, "store_name": "Tedi", "date": datetime.strptime(transaction_end_at, '%Y-%m-%dT%H:%M:%S').date() }
  
  return parsed_receipt