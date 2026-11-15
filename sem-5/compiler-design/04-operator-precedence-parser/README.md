# Practical 04: Operator Precedence Parser

## Objective
To implement an Operator Precedence Parser using operator precedence relation matrices (`<.`, `=.`, `.>`) for arithmetic expressions.

## Precedence Relations
- `a <. b`: Terminal `a` yields precedence to `b` (Shift).
- `a .> b`: Terminal `a` takes precedence over `b` (Reduce).
- `a =. b`: Terminal `a` has same precedence as `b` (e.g. `(` and `)`).

## Usage
```bash
python operator_precedence_parser.py "id + id * id"
```
