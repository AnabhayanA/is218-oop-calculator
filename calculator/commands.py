
"""Command objects for calculator actions."""

from calculator.factory import CalculationFactory
from calculator.history import History


class CalculateCommand:
    """Execute a calculation and save its result."""

    def __init__(self, operation: str, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b

    def execute(self, history: History) -> float:
        """Perform the requested calculation and record it."""
        calculation = CalculationFactory.create(
            self.operation, self.a, self.b
        )
        result = calculation.get_result()
        history.add(calculation, result)
        return result
