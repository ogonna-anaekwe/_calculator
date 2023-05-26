from _binary import Binary
from _group import Group
from _literal import Literal
from _unary import Unary
from _token_type import TokenType


class Parser:
    """Given a list a valid tokens that form an expression, generates AST for that expression.
    ASTs are generated through Recursive Descent parsing."""

    def __init__(self, tokens):
        self.tokens = tokens  # List of tokens (from the Scanner).
        self.current = 0  # Index of token being parsed.

    def parse(self):
        return self.expression()

    def expression(self):
        return self.term()

    def term(self):
        """BNF: term := factor(("+" | "-")factor)*"""
        expr = self.factor()

        while self.match([TokenType.PLUS.name, TokenType.MINUS.name]):
            operator = self.previous().lexeme
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self):
        """BNF: factor := unary(("/" | "*")unary)*"""
        expr = self.unary()

        while self.match([TokenType.SLASH.name, TokenType.STAR.name]):
            operator = self.previous().lexeme
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self):
        """BNF: unary := ("-"unary)* | power"""
        while self.match([TokenType.MINUS.name]):
            operator = self.previous().lexeme
            right = self.unary()  # unary is right-associative.
            return Unary(operator, right)

        return self.power()

    def power(self):
        """BNF: power := primary("^"power)*"""
        expr = self.primary()

        while self.match([TokenType.POWER.name]):
            operator = self.previous().lexeme
            right = self.power()  # exponentiation is right-associative.
            expr = Binary(expr, operator, right)

        return expr

    def primary(self):
        """Highest precedence represented by a literal (which in this case is TokenType.NUMBER) or a parenthesized expression.
        BNF: primary := NUMBER | "(" expression ")" """
        if self.match([TokenType.NUMBER.name]):
            return Literal(self.previous().lexeme)

        if self.match([TokenType.LEFT_PAREN.name]):
            expr = self.expression()
            self.check_token(
                TokenType.RIGHT_PAREN.name, "Missing closing ')' in group expression."
            )
            return Group(expr)

    def match(self, token_types):
        """Checks if token matches any of: +, -, /, *, ^, (, )."""
        for token_type in token_types:
            token_idx = self.current
            if self.at_end():
                token_idx -= 1  # Reaching the end of the tokens means we're 1 index higher, so we go back one step to grab the last token.

            tokens_match = self.tokens[token_idx].type == token_type
            if tokens_match:
                self.advance()
                return True

        return False

    def previous(self):
        """Return previous token."""
        return self.tokens[self.current - 1]

    def at_end(self):
        """Validate all tokens have been consumed."""
        return self.current == len(self.tokens)

    def advance(self):
        """Move to next token."""
        self.current += 1

    def check_token(self, token, err_msg):
        """Checks that the current token matches what's expected.
        This is used for matching the closing parenthesis for Group expressions."""
        token_idx = self.current

        if self.at_end():
            token_idx -= 1

        correct_token = self.tokens[token_idx].type == token
        if not correct_token:
            raise ValueError(err_msg)

        self.advance()
