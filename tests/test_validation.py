import pytest

from calculator.validation import numeric_values


def test_valid_numbers():
    assert numeric_values([2, 3]) == (2.0, 3.0)


def test_numeric_strings():
    assert numeric_values(["4", "5"]) == (4.0, 5.0)


def test_invalid_text():
    with pytest.raises(ValueError):
        numeric_values(["hello", 3])


def test_infinity():
    with pytest.raises(ValueError):
        numeric_values([float("inf"), 3])


def test_nan():
    with pytest.raises(ValueError):
        numeric_values([float("nan"), 3])


def test_none():
    with pytest.raises(ValueError):
        numeric_values([None, 3])