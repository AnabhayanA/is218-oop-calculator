"""A shared calculation contract and its concrete implementations."""
from calculator.composed_calculation import ComposedCalculation
from abc import ABC, abstractmethod
from calculator.operations import Operations


class Calculation(ABC):
    """Store two operands and require subclasses to provide a result."""

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    @abstractmethod
    def get_result(self) -> float:
        """Return the result of this calculation."""


class Add(Calculation):
    """Add the two operands using composition."""

    def get_result(self) -> float:
        calculation = ComposedCalculation(
            self.a,
            self.b,
            Operations.add
        )
        return calculation.get_result()


class Subtract(Calculation):
    """Subtract the second operand from the first."""

    def get_result(self) -> float:
        return Operations.subtract(self.a, self.b)