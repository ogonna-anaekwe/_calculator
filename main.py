from _evaluator import Evaluator
from _parser import Parser
from _scanner import Scanner
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "expr",
        help='expression that you\'d like to evaluate. e.g: "10 * 50 ^ 2 - 40". it must be wrapped in double quotes.',
    )
    string = parser.parse_args().expr
    scanner = Scanner(string)
    tokens = scanner.scan()
    parser = Parser(tokens)
    expression = parser.parse()
    print(Evaluator().evaluate(expression))
