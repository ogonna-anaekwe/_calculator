class Binary:
    """Binary node in the AST.
    Every binary operation must have an operator with an operand on either side."""

    lisp_style = True

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        """Interface to the visitor implementation for Binary Expressions."""
        return visitor.visit_binary_expr(self)

    def __str__(self):
        """Overrides default str representation."""
        binary_ast = binary_ast = "".join(
            [
                "(",
                str(self.operator),
                " ",
                str(self.left),
                " ",
                str(self.right),
                ")",
            ]
        )
        if Binary.lisp_style:
            return binary_ast

        binary_ast = "".join(
            [
                "Binary[",
                str(self.left),
                ", ",
                str(self.operator),
                ", ",
                str(self.right),
                "]",
            ]
        )

        return binary_ast
