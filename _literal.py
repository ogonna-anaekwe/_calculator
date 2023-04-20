class Literal:
    """Literal node in the AST.
    A Literal is just a expression waiting to returned as a value."""

    lisp_style = True

    def __init__(self, value):
        self.value = value

    def accept(self, Visitor):
        """Interface to the visitor implementation for Literal Expressions."""
        return Visitor.visit_literal_expr(self)

    def __str__(self):
        """Overrides default str representation."""
        literal_ast = "".join([str(self.value)])

        if Literal.lisp_style:
            return literal_ast

        literal_ast = "".join(
            [
                "Literal[",
                str(self.value),
                "]",
            ]
        )

        return literal_ast
