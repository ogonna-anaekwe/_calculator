from _visitor import Visitor


class Evaluator(Visitor):
    """Evaluates a string representation of an arithmetic expression."""

    precision = 2  # Since we use floating point numbers for all numbers, this determines the number of decimal places to show after evaluation.

    def __init__(self):
        pass

    def evaluate(self, expression):
        """Evaluate the given expression via double dispatch."""
        return expression.accept(self)

    def visit_binary_expr(self, Binary):
        """Visitor implementation for binary expressions."""
        left = self.evaluate(Binary.left)
        right = self.evaluate(Binary.right)

        self.check_operands(left, right)

        left = float(left)
        right = float(right)

        if Binary.operator == "+":
            return round(left + right, Evaluator.precision)

        if Binary.operator == "-":
            return round(left - right, Evaluator.precision)

        if Binary.operator == "/":
            return round(left / right, Evaluator.precision)

        if Binary.operator == "*":
            return round(left * right, Evaluator.precision)

        if Binary.operator == "^":
            return round(pow(left, right), Evaluator.precision)

    def visit_literal_expr(self, Literal):
        """Visitor implementation for literal expressions."""
        return Literal.literal

    def check_operands(self, left, right):
        """Validate that both the left and right operands are numbers."""
        if not (isinstance(float(left), float) and isinstance(float(right), float)):
            raise TypeError("Left and right operands must be numbers.")
