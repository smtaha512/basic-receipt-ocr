from fuzzywuzzy import fuzz


def best_match_within_accuracy(
    best_match: str, highest_score: int, max_accuracy=70, min_accuracy=40
) -> str | None:
    if max_accuracy < min_accuracy:
        return None

    return (
        best_match
        if highest_score >= max_accuracy
        else best_match_within_accuracy(
            best_match,
            highest_score,
            max_accuracy=(max_accuracy - max_accuracy / 10),
            min_accuracy=min_accuracy,
        )
    )


def fuzzy_match(
    extracted_name, expected_strings, max_accuracy=100, min_accuracy=40
) -> str | None:
    best_match = None
    highest_score = 0
    for string in expected_strings:
        score = fuzz.ratio(extracted_name.lower(), string.lower())
        if score > highest_score:
            highest_score = score
            best_match = string
    # Return the best match if similarity is between a range
    return best_match_within_accuracy(
        best_match, highest_score, max_accuracy, min_accuracy
    )


def get_index_by_fuzzy_match(
    receipt_content: list[str], expected_strings: list[str]
) -> int:
    return receipt_content.index(
        next(
            filter(
                lambda item: fuzzy_match(item, expected_strings) is not None,
                receipt_content,
            )
        )
    )
