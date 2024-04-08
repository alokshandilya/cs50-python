from bank import value


def test_lowercase():
    assert value("hello alok shandilya") == 0
    assert value("hi alok shandilya") == 20
    assert value("hey alok shandilya") == 20
    assert value("mr alok shandilya") == 100


def test_uppercase():
    assert value("HELLO ALOK SHANDILYA") == 0
    assert value("HI ALOK SHANDILYA") == 20
    assert value("MR ALOK SHANDILYA") == 100


def test_punctuation():
    assert value("Hello, Alok Shandilya") == 0
    assert value("HI, ALOK SHANDILYA") == 20
    assert value("mr. alok shandilya") == 100
