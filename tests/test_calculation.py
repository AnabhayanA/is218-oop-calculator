"""Tests for the calculator calculation classes."""

import pytest

from calculator.calculation import Add, Calculation, Subtract


def test_add():
    calculation = Add(10, 5)
    result = calculation.get_result()
    assert result == 15


def test_instances_have_their_own_operands():
    first = Add(10, 5)
    second = Add(100, 50)

    first.a = 20

    assert first.get_result() == 25
    assert second.a == 100
    assert second.b == 50
    assert second.get_result() == 150


def test_negative_operand():
    assert Add(-10, 5).get_result() == -5


def test_zero_operands():
    assert Add(0, 0).get_result() == 0


def test_mixed_operands_remain_unchanged():
    calculation = Add(12, -4)

    result = calculation.get_result()

    assert result == 8
    assert calculation.a == 12
    assert calculation.b == -4


def test_subtract():
    assert Subtract(20, 7).get_result() == 13


def test_subtract_can_return_a_negative_result():
    assert Subtract(5, 10).get_result() == -5


def test_calculation_is_abstract():
    with pytest.raises(TypeError):
        Calculation(10, 5)


def test_polymorphism():
    calculations = [Add(10, 5), Subtract(20, 7)]
    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [15, 13]

def test_three_calculations_with_polymorphism():
    calculations = [
        Add(7, 3),
        Subtract(4, 9),
        Add(15, 5),
    ]

    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [10, -5, 20]