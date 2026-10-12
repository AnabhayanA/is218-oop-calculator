
"""Factory for creating calculator operations."""

from calculator.calculation import Add, Calculation, Subtract


class CalculationFactory:
    """Create calculation objects from operation names."""

    _operations = {
        "add": Add,
        "subtract": Subtract,
    }

    @classmethod
    def create(
        cls, operation: str, *values: float, **options
    ) -> Calculation:
        """Create a calculation using flexible arguments."""
        if not isinstance(operation, str):
            raise ValueError("Operation must be a string.")

        name = operation.strip().lower()

        if name not in cls._operations:
            raise ValueError(f"Unknown operation: {operation}")

        return cls._operations[name](*values, **options)
