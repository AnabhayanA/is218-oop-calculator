"""A calculation that stores its operation as a callable."""

from calculator.operations import Operations


class ComposedCalculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        return self.operation(self.a, self.b)