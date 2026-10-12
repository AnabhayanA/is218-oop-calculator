
"""Tests for the calculation factory."""

import pytest

from calculator.calculation import Add, Subtract
from calculator.factory import CalculationFactory


def test_factory_creates_add():
    calculation = CalculationFactory.create("add", 10, 5)

    assert isinstance(calculation, Add)
    assert calculation.get_result() == 15


def test_factory_creates_subtract():
    calculation = CalculationFactory.create("subtract", 10, 5)

    assert isinstance(calculation, Subtract)
    assert calculation.get_result() == 5


def test_factory_is_case_insensitive():
    calculation = CalculationFactory.create(" ADD ", 2, 3)

    assert calculation.get_result() == 5


def test_factory_rejects_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("divide", 10, 2)


def test_factory_rejects_non_string_operation():
    with pytest.raises(ValueError, match="Operation must be a string"):
        CalculationFactory.create(None, 10, 2)
