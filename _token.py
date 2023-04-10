class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme

    def __str__(self):
        """Calling print on a Token gives the type + lexeme"""
        return " ".join([self.type, self.lexeme])
