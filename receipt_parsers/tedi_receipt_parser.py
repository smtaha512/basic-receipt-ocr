from datetime import datetime
import re

def chunks(items: list[str], chunk_size: int):
  for i in range(0, len(items), chunk_size):
    yield items[i:i + chunk_size]

def parse_receipt(texts: list[str]):
  receipt_content = list(map(lambda text: text.description, texts))[0].split("\n")
  
  index_of_first_item = 5
  index_of_last_item_price = receipt_content.index("Kaufsumme:") - 1
  
  items = receipt_content[index_of_first_item : index_of_last_item_price + 1]
  dict_of_items = list(map(lambda item: { "serial_no": item[0], "name": item[1], "price": float(item[2]) }, list(chunks(items, 3))))
  
  transaction_end_at = [item for _, item in enumerate(receipt_content) if re.search('\d{4}-\d{2}-\d{2}T\d{2}', item)][1:2][0]
  
  return { "items": dict_of_items, "store_name": "Tedi", "date": datetime.strptime(transaction_end_at, '%Y-%m-%dT%H:%M:%S').date() }