from enum import Enum


class TokenType(Enum):
    # Operators, Left-Right Parenthesis, and Number literal.
    PLUS, MINUS, SLASH, STAR, POWER, LEFT_PAREN, RIGHT_PAREN, NUMBER = range(0, 8)
