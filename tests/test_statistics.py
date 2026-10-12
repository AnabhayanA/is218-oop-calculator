
"""Tests for statistical operations."""

import pytest

from calculator.statistics import Statistics


def test_total():
    assert Statistics.total(1, 2, 3, 4) == 10


def test_mean():
    assert Statistics.mean(2, 4, 6) == 4


def test_stddev():
    assert Statistics.stddev(2, 4, 6) == pytest.approx(2)


def test_stddev_large_values():
    result = Statistics.stddev(1e308, -1e308)
    assert result > 0


@pytest.mark.parametrize(
    "method, values",
    [
        (Statistics.total, ()),
        (Statistics.mean, ()),
        (Statistics.stddev, (5,)),
        (Statistics.mean, ("abc", 2)),
        (Statistics.total, (float("inf"), 2)),
        (Statistics.total, (1e308, 1e308)),
    ],
)
def test_invalid_statistics(method, values):
    with pytest.raises(ValueError):
        method(*values)
