## Overview
This is a calculator that evaluates basic arithmetic operations: addition `+`, subtraction `-`, division `/`, multiplication `*`, and power `^`.

## How it works
A user passes a string representation of an arithmetic operation (e.g. `"10 / 5 + 6 * 88"`). We take that string and proceed thus:
1. scan every character to generate a list of tokens. 
2. parse the list (from step 1) to generate an [Abstract Syntax Tree (AST)](https://en.wikipedia.org/wiki/Abstract_syntax_tree) for the user-inputted arithmetic operation.
3. evaluate the AST. 

All 3 steps are implemented by `Scanner`, `Parser`, and `Evaluator` respectively.

## Grammar
We use [a BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) for our grammar. In the grammar rules below, quoted and capitalized objects (e.g. `"+"`, `NUMBER`) are terminals, the rest are non-terminals.
```sh
expression -> literal | binary | group | unary;
literal -> NUMBER;
binary -> expression operator expression;
group -> "(" expression ")";
unary -> "-"expression
operator -> "+" | "-" | "/" | "*" | "^";
```

To determine precedence and associativity (i.e the order in which operations will be evaluated), we expand the grammar thus:
```sh
expression -> term;
term -> factor ( ( "+" | "-" ) factor )*;
factor -> unary ( ( "/" | "*" ) unary )*;
unary -> ( "-" unary )* | power;
power -> primary ( "^" power )*;
primary -> NUMBER | "(" expression ")";
```

All rules are [left-associative](https://en.wikipedia.org/wiki/Operator_associativity) but the `unary` and `power` rules which are right-associative.

## Usage
```sh
python main.py "<arithmetic_operation>" # python main.py "10 / 5 + 6 * 88"
```
