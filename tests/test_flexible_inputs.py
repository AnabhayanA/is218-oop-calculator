
"""Tests for flexible operation inputs."""

import pytest

from calculator.calculation import Add
from calculator.factory import CalculationFactory
from calculator.operations import Operations


def test_add_multiple_values():
    assert Operations.add(2, 3, 4, 5) == 14


def test_subtract_multiple_values():
    assert Operations.subtract(20, 3, 2) == 15


def test_multiply_multiple_values():
    assert Operations.multiply(2, 3, 4) == 24


def test_divide_multiple_values():
    assert Operations.divide(100, 2, 5) == 10


def test_divide_multiple_values_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(100, 2, 0)


def test_total_multiple_values():
    assert Operations.total(1, 2, 3, 4) == 10


def test_total_with_start_option():
    assert Operations.total(1, 2, 3, start=10) == 16


def test_total_with_no_values():
    assert Operations.total() == 0


def test_factory_accepts_positional_values():
    calculation = CalculationFactory.create("add", 2, 3)
    assert isinstance(calculation, Add)
    assert calculation.get_result() == 5


def test_factory_accepts_keyword_options():
    calculation = CalculationFactory.create("add", a=2, b=3)
    assert calculation.get_result() == 5
