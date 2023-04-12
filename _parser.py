from _binary import Binary
from _literal import Literal
from _token_type import TokenType


class Parser:
    """Given a list a valid tokens that form an expression, generates AST for that expression.
    ASTs are generated through Recursive Descent parsing."""

    def __init__(self, tokens):
        self.tokens = tokens  # List of tokens (from the Scanner).
        self.current = 0  # Index of token being parsed.

    def parse(self):
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
        """BNF: factor := power(("/" | "*")power)*"""
        expr = self.power()

        while self.match([TokenType.SLASH.name, TokenType.STAR.name]):
            operator = self.previous().lexeme
            right = self.power()
            expr = Binary(expr, operator, right)

        return expr

    def power(self):
        """BNF: power := primary("^"primary)*"""
        expr = self.primary()

        while self.match([TokenType.POWER.name]):
            operator = self.previous().lexeme
            right = self.primary()
            expr = Binary(expr, operator, right)

        return expr

    def primary(self):
        """Highest precedence represented by a literal which in this case is TokenType.NUMBER.
        BNF: primary := NUMBER"""
        if self.at_end():
            return Literal(self.previous().lexeme)

        self.advance()  # Remove this and see what happens.
        return Literal(self.previous().lexeme)

    def match(self, token_types):
        """Checks if token matches any of the arithmetic operators: +, -, /, *, ^."""
        for token_type in token_types:
            token_idx = self.current
            if self.at_end():
                token_idx -= 1  # Reaching the end of the tokens means we're 1 index higher, so we go back one step to grab the last token.

            tokens_match = self.tokens[token_idx].type == token_type
            if tokens_match:
                self.advance()
                return True

        # No need to call advance() here since tokens that don't match eventually
        # hit primary() which calls advance(). Calling advance() here
        # will lead to an IndexError.
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

    def check_syntax(self):
        pass
