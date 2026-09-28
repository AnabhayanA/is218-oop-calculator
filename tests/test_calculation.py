"""A first test checks an observable result with a direct assertion."""

from calculator.calculation import Add


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