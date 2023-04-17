from enum import Enum


class TokenType(Enum):
    # Operators and Number Literal.
    PLUS, MINUS, SLASH, STAR, POWER, LEFT_PAREN, RIGHT_PAREN, NUMBER = range(0, 8)
