class Group:
    """Group node in the AST. A Group is a parenthesized expression."""

    lisp_style = True

    def __init__(self, expression):
        self.expression = expression

    def accept(self, Visitor):
        """Interface to the visitor implementation for Group Expressions."""
        return Visitor.visit_group_expr(self)

    def __str__(self):
        """Overrides default str representation."""
        group_ast = "".join([str(self.expression)])

        if Group.lisp_style:
            return group_ast

        group_ast = "".join(
            [
                "Group[",
                str(self.expression),
                "]",
            ]
        )

        return group_ast
