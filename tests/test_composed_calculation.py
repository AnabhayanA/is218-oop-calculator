from calculator.composed_calculation import ComposedCalculation


def test_operation_runs_only_when_requested():
    calls = []

    def spy_operation(a, b):
        calls.append((a, b))
        return a + b

    calculation = ComposedCalculation(2, 3, spy_operation)

    assert calls == []

    result = calculation.get_result()

    assert result == 5
    assert calls == [(2, 3)]