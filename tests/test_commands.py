
"""Tests for calculator commands."""

import pytest

from calculator.commands import CalculateCommand
from calculator.history import History


def test_add_command():
    history = History()
    command = CalculateCommand("add", 2, 3)

    assert command.execute(history) == 5
    assert history.get_results() == [5]


def test_subtract_command():
    history = History()
    command = CalculateCommand("subtract", 10, 4)

    assert command.execute(history) == 6
    assert history.get_results() == [6]


def test_command_rejects_unknown_operation():
    history = History()
    command = CalculateCommand("unknown", 2, 3)

    with pytest.raises(ValueError, match="Unknown operation"):
        command.execute(history)

    assert history.get_history() == []


def test_command_does_not_save_failed_calculation():
    history = History()
    command = CalculateCommand("add", float("inf"), 3)

    with pytest.raises(ValueError):
        command.execute(history)

    assert history.get_results() == []
