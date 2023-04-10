from _token import Token
from _token_type import TokenType


# BUG: ending w/ an int btw 1 - 9 makes the scanner drop the int.
class Scanner:
    """Given a sequence of lexemes, creates a list of tokens."""

    operators = {
        "+": TokenType.PLUS,
        "-": TokenType.MINUS,
        "/": TokenType.SLASH,
        "*": TokenType.STAR,
        "^": TokenType.POWER,
    }

    def __init__(self, string):
        self.string = string  # This is the expression we scan for tokens.
        self.tokens = []  # Stores valid tokens.
        self.digits = []  # Stores all digits in multi-digit numbers.
        self.current = 0  # Index of the character that the scanner is on.

    def scan(self):
        """Until we reach the end of the input string/expression, keep creating valid tokens from lexemes: numbers and basic arithmetic operators.
        Every other lexeme is ignored."""
        while not self.at_end():
            operator = Scanner.operators.get(self.string[self.current])
            is_digit_or_dot = self.is_digit_or_dot(self.string[self.current])

            if operator:
                self.add_token(operator.name, self.string[self.current])

            if is_digit_or_dot:
                self.digits = []
                number = self.get_digit()
                self.add_token(TokenType.NUMBER.name, number)

            self.advance()

        # self.validate_tokens()
        return self.tokens

    def add_token(self, token_type, lexeme):
        """Adds token object to list of tokens."""
        token = Token(token_type, lexeme)
        self.tokens.append(token)

    def advance(self):
        """Increments position to help navigate to the next character."""
        self.current += 1

    def is_digit(self, c):
        """Checks whether character is a digit."""
        return c >= "0" and c <= "9"

    def is_dot(self, c):
        """Checks whether character is a dot. Used for floating point numbers."""
        return c == "."

    def is_digit_or_dot(self, c):
        """Checks whether character is digit or dot. Used to capture both integers and floating point numbers."""
        return self.is_digit(c) or self.is_dot(c)

    def get_digit(self):
        """(Recursively) scans single/multi-digit integers or floating point numbers"""
        self.digits.append(self.string[self.current])
        if not self.at_end():
            next_is_digit_or_dot = self.is_digit_or_dot(self.next())
            if next_is_digit_or_dot:
                self.advance()
                self.get_digit()  # Recursively walk through the string of chars to get multi-digit numbers.

        return "".join(self.digits)

    def next(self):
        """Returns next character. Returns '-1' if we've reach the End of String."""
        if self.at_end():
            return "-1"

        return self.string[self.current + 1]

    def at_end(self):
        """Checks if we've reached the end of the input string/expression."""
        return self.current >= len(self.string) - 1

    def validate_tokens(self):
        """Checks that the tokens extracted form a valid arithmetic operation."""
        num_first = self.is_digit(self.tokens[0].lexeme)
        num_last = self.is_digit(self.tokens[-1].lexeme)
        if not num_first or not num_last:
            raise ValueError("Expressions must start and end with a number.")

        token_len = len(self.tokens)
        for idx in range(token_len):
            if idx % 2 == 0:  # Even indexed tokens must be numbers (i.e. operands).
                is_digit = self.is_digit_or_dot(self.tokens[idx].lexeme)
                if not is_digit:
                    raise ValueError("Number expected for token number " + str(idx))

            else:  # Odd-indexed tokens must be operators.
                is_operator = Scanner.operators.get(self.tokens[idx].lexeme)
                if not is_operator:
                    raise ValueError("Operator expected for token number " + str(idx))

    def print_tokens(self):
        for token in self.tokens:
            print(token)
