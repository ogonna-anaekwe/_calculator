# _calculator
This is a calculator that evaluates basic arithmetic operations: addition `+`, subtraction `-`, division `\`, multiplication `\*`, and power `^`.
> keywords: Backus-Naur Form (BNF), Abstract Syntax Tree (AST), Recursive Descent parsing

# How it works
A user passes a string representation of an arithmetic operation. E.g. `"10 / 5 + 6 * 88"`. We scan every character in that string to generate tokens. We then parse the token to generate an AST for the user-inputted arithmetic operation. Finally, we evaluate the AST. These 3 steps are implemented by helper classes: `Scanner`, `Parser`, and `Evaluator` respectively.

# Usage
```sh
python main.py "<arithmetic_operation>" # python main.py "10 / 5 + 6 * 88"
```
