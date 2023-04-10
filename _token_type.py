from enum import Enum


class TokenType(Enum):
    # Operators and Number Literal.
    PLUS, MINUS, SLASH, STAR, POWER, NUMBER = range(0, 6)
