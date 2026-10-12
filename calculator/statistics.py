
"""Statistical calculations on finite numeric values."""

from statistics import mean as statistics_mean
from statistics import stdev

from calculator.validation import numeric_values


class Statistics:
    """Provide sum, mean, and sample standard deviation."""

    @staticmethod
    def total(*values: float) -> float:
        numbers = numeric_values(values)
        if not numbers:
            raise ValueError("At least one number is required.")
        result = sum(numbers)
        return numeric_values((result,))[0]

    @staticmethod
    def mean(*values: float) -> float:
        numbers = numeric_values(values)
        if not numbers:
            raise ValueError("At least one number is required.")
        result = statistics_mean(numbers)
        return numeric_values((result,))[0]

    @staticmethod
    def stddev(*values: float) -> float:
        numbers = numeric_values(values)
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required.")
        result = stdev(numbers)
        return numeric_values((result,))[0]
