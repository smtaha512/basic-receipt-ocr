def chunks(items: list[str], chunk_size: int):
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]
