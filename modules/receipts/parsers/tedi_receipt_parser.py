import re
from datetime import datetime

from .types.parsed_receipt_type import Item, ParsedReceipt
from .utils.chunks import chunks
from .utils.fuzzy_match import get_index_by_fuzzy_match


def parse_receipt(receipt_content: list[str]) -> ParsedReceipt:
    index_of_first_item = 5

    excepted_keywords_for_total = ["Summe", "Total", "Kaufsumme", "Kaufsunm3"]
    index_of_last_item_price = (
        get_index_by_fuzzy_match(receipt_content, excepted_keywords_for_total) - 1
    )

    items = receipt_content[index_of_first_item : index_of_last_item_price + 1]

    item_rows = chunks(items, 3)
    mapped_items: map[Item] = map(
        lambda item: {
            "serial_no": item[0],
            "name": item[1],
            "quantity": 1,
            "price_per_item": float(item[2]),
            "total": float(item[2]),
        },
        item_rows,
    )

    transaction_end_at: str = [
        item
        for _, item in enumerate(receipt_content)
        if re.search("\d{4}-\d{2}-\d{2}T\d{2}", item)
    ][1:2][0]

    parsed_receipt: ParsedReceipt = {
        "items": [*mapped_items],
        "store_name": "TEDI",
        "date": datetime.strptime(transaction_end_at, "%Y-%m-%dT%H:%M:%S").date(),
    }

    return parsed_receipt
