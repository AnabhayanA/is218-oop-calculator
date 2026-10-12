
"""Integration tests for extended arithmetic operations."""

import pytest

from calculator.calculation import Divide, Multiply
from calculator.commands import CalculateCommand
from calculator.factory import CalculationFactory
from calculator.history import History


def test_multiply_calculation():
    assert Multiply(6, 7).get_result() == 42


def test_divide_calculation():
    assert Divide(20, 4).get_result() == 5


def test_factory_creates_multiply():
    calculation = CalculationFactory.create("multiply", 3, 8)
    assert isinstance(calculation, Multiply)
    assert calculation.get_result() == 24


def test_factory_creates_divide():
    calculation = CalculationFactory.create("divide", 18, 3)
    assert isinstance(calculation, Divide)
    assert calculation.get_result() == 6


def test_multiply_command_saves_history():
    history = History()
    result = CalculateCommand("multiply", 4, 5).execute(history)

    assert result == 20
    assert history.get_results() == [20]


def test_divide_command_saves_history():
    history = History()
    result = CalculateCommand("divide", 20, 5).execute(history)

    assert result == 4
    assert history.get_results() == [4]


def test_divide_by_zero_does_not_save_history():
    history = History()

    with pytest.raises(ZeroDivisionError):
        CalculateCommand("divide", 10, 0).execute(history)

    assert history.get_history() == []
    assert history.get_results() == []
