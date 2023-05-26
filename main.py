from _evaluator import Evaluator
from _parser import Parser
from _scanner import Scanner
import argparse
import sys

if __name__ == "__main__":
    sys.tracebacklimit = 0  # Print last line in error stack trace.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "expr",
        help='expression that you want to evaluate. e.g: "10 * 50 ^ 2 - 40". it must be wrapped in double quotes.',
    )
    string = "".join(
        [parser.parse_args().expr, " "]
    )  # " " because of a bug in the Scanner: For expressions ending w/ an int btw 0 - 9, the Scanner drops the int, resulting in an invalid sequence of tokens.
    scanner = Scanner(string)
    tokens = scanner.scan()
    ast = Parser(tokens).parse()
    value = Evaluator().evaluate(ast)
    print(value)
