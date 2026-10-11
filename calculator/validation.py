"""Validate numeric operands for calculations."""

from math import isfinite


def numeric_values(values):
    numbers = []

    for value in values:
        try:
            number = float(value)
        except (TypeError, ValueError) as error:
            raise ValueError("A numeric value is required.") from error

        if not isfinite(number):
            raise ValueError("A finite number is required.")

        numbers.append(number)

    return tuple(numbers)