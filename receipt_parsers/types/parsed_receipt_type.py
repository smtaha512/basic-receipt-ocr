from datetime import date
from types import MappingProxyType
from typing import Dict, Literal, TypedDict

Tedi = Literal['TEDI']
Edeka = Literal['Edeka']

Item = TypedDict('Item', serial_no=str | None, name=str, total=float, quantity=int, price_per_item=float)

ParsedReceipt = TypedDict("ParsedReceipt",
  items=list[Item],
  date=date,
  store_name=Tedi | Edeka,
)