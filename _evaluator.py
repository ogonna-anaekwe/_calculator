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

        Evaluator.check_operands(left, right)

        left = float(left)
        right = float(right)

        if Binary.operator == "+":
            return round(left + right, Evaluator.precision)

        if Binary.operator == "-":
            return round(left - right, Evaluator.precision)

        if Binary.operator == "/":
            if right == 0:
                raise ZeroDivisionError("Can't divide by 0.")

            return round(left / right, Evaluator.precision)

        if Binary.operator == "*":
            return round(left * right, Evaluator.precision)

        if Binary.operator == "^":
            return round(pow(left, right), Evaluator.precision)

    def visit_literal_expr(self, Literal):
        """Visitor implementation for literal expressions."""
        return Literal.value

    def visit_group_expr(self, Group):
        """Visitor implementation for group/parenthesized expressions."""
        return self.evaluate(
            Group.expression
        )  # Must evaluate the expression to avoid stack overflow! Stack overflow occurs if you evaluate the Group. Drop .expression and see!

    @staticmethod
    def check_operands(left, right):
        """Validate that both the left and right operands are numbers."""
        if not (isinstance(float(left), float) and isinstance(float(right), float)):
            raise TypeError("Left and right operands must be numbers.")
