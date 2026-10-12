
"""Factory for creating calculation objects."""

from calculator.calculation import Add, Divide, Multiply, Subtract


class CalculationFactory:
    """Create calculation objects from operation names."""

    @staticmethod
    def create(operation: str, *values: float, **options):
        """Create a calculation while validating its operation name."""

        if not isinstance(operation, str):
            raise ValueError("Operation must be a string.")

        operation = operation.strip().lower()

        operations = {
            "add": Add,
            "subtract": Subtract,
            "multiply": Multiply,
            "divide": Divide,
        }

        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")

        return operations[operation](*values, **options)
