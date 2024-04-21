from seasons import calculate_age, age_in_words


def test_calculate_age():
    assert calculate_age(2000, 6, 11) == 12540960


def test_age_in_words():
    assert (
        age_in_words(12540960)
        == "Twelve million, five hundred forty thousand, nine hundred sixty minutes"
    )
