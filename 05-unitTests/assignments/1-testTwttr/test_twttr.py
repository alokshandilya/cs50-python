from twttr import shorten


def test_vowels_lowercase():
    assert shorten("hello") == "hll"


def test_vowels_uppercase():
    assert shorten("HELLO") == "HLL"


def test_punctuation():
    assert shorten("Hello, World") == "Hll, Wrld"


def test_numbers():
    assert shorten("Hello, 7") == "Hll, 7"
