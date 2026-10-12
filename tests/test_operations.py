
import pytest

from calculator.operations import Operations


def test_add():
    assert Operations.add(2, 3) == 5


def test_subtract():
    assert Operations.subtract(10, 4) == 6


def test_multiply():
    assert Operations.multiply(3, 4) == 12


def test_divide():
    assert Operations.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(10, 0)


def test_absolute_difference_positive():
    assert Operations.absolute_difference(10, 4) == 6


def test_absolute_difference_reverse():
    assert Operations.absolute_difference(4, 10) == 6


def test_absolute_difference_negative():
    assert Operations.absolute_difference(-3, 5) == 8
