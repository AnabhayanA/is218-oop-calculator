
from calculator.calculation import Calculation


class History:
    def __init__(self):
        self._calculations: list[Calculation] = []
        self._results: list[float] = []

    def add(self, calculation: Calculation, result: float | None = None) -> None:
        if not isinstance(calculation, Calculation):
            raise TypeError("History only accepts Calculation objects")

        if result is None:
            result = calculation.get_result()

        self._calculations.append(calculation)
        self._results.append(result)

    def get_history(self) -> list[Calculation]:
        return self._calculations.copy()

    def get_results(self) -> list[float]:
        """Return a copy of the saved calculation results."""
        return self._results.copy()

    def remove(self, index: int) -> Calculation:
        if index < 0 or index >= len(self._calculations):
            raise IndexError("History index out of range")

        self._results.pop(index)
        return self._calculations.pop(index)
