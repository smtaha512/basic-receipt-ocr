import locale
import re
from datetime import datetime

from .types.parsed_receipt_type import Item, ParsedReceipt
from .utils.chunks import chunks


def convert_euro_currency_to_float(price: str) -> float:
    locale.setlocale(locale.LC_ALL, "de_DE")
    return locale.atof(price)


def item_to_dict(item: list[str]) -> Item:
    total = convert_euro_currency_to_float(item[1].split(" A")[0])

    index_of_quantity_and_price = [
        (match.start()) for match in re.finditer("\d+,\d+.EUR.\d", item[0])
    ]

    name = (
        item[0]
        if len(index_of_quantity_and_price) < 1
        else item[0][: index_of_quantity_and_price[0] - 1]
    )

    price_per_item = total
    quantity = 1

    if len(index_of_quantity_and_price) > 0:
        [price_per_item, quantity] = (item[0][index_of_quantity_and_price[0] :]).split(
            "EUR"
        )

        price_per_item = convert_euro_currency_to_float(price_per_item)

    return {
        "name": name,
        "price_per_item": price_per_item,
        "total": total,
        "quantity": quantity,
        "serial_no": None,
    }


def parse_receipt(receipt_content: list[str]) -> ParsedReceipt:
    index_of_first_item = 4
    index_of_last_item_price = (
        receipt_content.index(
            [i for i in receipt_content if re.findall("Posten:", i)][0]
        )
        - 1
    )

    items = receipt_content[index_of_first_item : index_of_last_item_price + 1]
    item_rows = chunks(items, 2)

    mapped_items: map[Item] = map(item_to_dict, item_rows)

    transaction_end_at: str = [
        item
        for _, item in enumerate(receipt_content)
        if re.search("\d{2}\.\d{2}\.\d{2}", item)
    ][0]

    parsed_receipt: ParsedReceipt = {
        "items": [*mapped_items],
        "store_name": "Edeka",
        "date": datetime.strptime(transaction_end_at, "%d.%m.%Y").date(),
    }

    return parsed_receipt
