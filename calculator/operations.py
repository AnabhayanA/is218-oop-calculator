
"""Mathematical operations for the calculator."""

from math import prod


class Operations:
    """Group mathematical operations."""

    @staticmethod
    def add(a: float, b: float, *values: float) -> float:
        return a + b + sum(values)

    @staticmethod
    def subtract(a: float, b: float, *values: float) -> float:
        result = a - b
        for value in values:
            result -= value
        return result

    @staticmethod
    def multiply(a: float, b: float, *values: float) -> float:
        return a * b * prod(values)

    @staticmethod
    def divide(a: float, b: float, *values: float) -> float:
        result = a / b
        for value in values:
            result /= value
        return result

    @staticmethod
    def absolute_difference(a: float, b: float) -> float:
        """Return the positive difference between two numbers."""
        return abs(a - b)

    @staticmethod
    def total(*values: float, start: float = 0) -> float:
        """Add any number of values, optionally using a starting value."""
        return sum(values, start)
