class Unary:
    """Unary node in the AST."""

    lisp_style = True

    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def accept(self, Visitor):
        """Interface to the visitor implementation for Unary Expressions."""
        return Visitor.visit_unary_expr(self)

    def __str__(self):
        """Overrides default str representation."""
        unary_ast = "".join(["(", self.operator, " ", str(self.right), ")"])

        if Unary.lisp_style:
            return unary_ast

        unary_ast = "".join(
            [
                "Unary[",
                str(self.right),
                "]",
            ]
        )

        return unary_ast
