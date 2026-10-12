
"""A shared calculation contract and its concrete implementations."""

from abc import ABC, abstractmethod

from calculator.composed_calculation import ComposedCalculation
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
    """Add two operands using composition."""

    def get_result(self) -> float:
        return ComposedCalculation(
            self.a, self.b, Operations.add
        ).get_result()


class Subtract(Calculation):
    """Subtract two operands using composition."""

    def get_result(self) -> float:
        return ComposedCalculation(
            self.a, self.b, Operations.subtract
        ).get_result()


class Multiply(Calculation):
    """Multiply two operands using composition."""

    def get_result(self) -> float:
        return ComposedCalculation(
            self.a, self.b, Operations.multiply
        ).get_result()


class Divide(Calculation):
    """Divide two operands using composition."""

    def get_result(self) -> float:
        return ComposedCalculation(
            self.a, self.b, Operations.divide
        ).get_result()
