# _calculator
This is a calculator that evaluates basic arithmetic operations: addition `+`, subtraction `-`, division `\`, multiplication `\*`, and power `^`.
> keywords: Backus-Naur Form (BNF), Abstract Syntax Tree (AST), Recursive Descent parsing

# How it works
A user passes a string representation of an arithmetic operation. E.g. `"10 / 5 + 6 * 88"`. We scan every character in that string to generate tokens. We then parse the token to generate an AST for the user-inputted arithmetic operation. Finally, we evaluate the AST. These 3 steps are implemented by helper classes: `Scanner`, `Parser`, and `Evaluator` respectively.

# Grammar
We use [a BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) for our grammar. In the grammar rules below, quoted and capitalized objects (e.g. `"+"`, `NUMBER`) are terminals, the rest are non-terminals.
```sh
expression -> literal | binary;
literal -> NUMBER;
binary -> expression operator expression;
operator -> "+" | "-" | "/" | "*";
```

To determine precedence (i.e the order in which operations will be evaluated), we expand the grammar to:
```sh
expression -> term;
term -> factor(("+" | "-") factor)*;
factor -> power(("/" | "*") power)*;
power -> primary("^"primary)*;
primary -> NUMBER
```

# Usage
```sh
python main.py "<arithmetic_operation>" # python main.py "10 / 5 + 6 * 88"
```
