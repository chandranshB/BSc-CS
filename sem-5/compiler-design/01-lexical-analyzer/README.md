# Practical 01: Lexical Analyzer (Scanner)

## Objective
To implement a lexical analyzer (scanner) in Python that reads source code, strips single-line and multi-line comments, identifies valid tokens according to language lexical rules, reports unrecognized characters, and builds a symbol table.

## Features
- **Token Classification**:
  - Keywords (`int`, `float`, `char`, `if`, `while`, `return`, etc.)
  - Identifiers (`main`, `fact`, `num`, etc.)
  - Integer and Float Constants (`5`, `120.0`, `1.0`)
  - String and Character Literals (`"..."`, `'A'`)
  - Operators: Arithmetic (`+`, `-`, `*`, `/`), Relational (`==`, `!=`, `<=`, `>=`), Logical (`&&`, `||`), Increment/Decrement (`++`, `--`), Assignment (`=`, `+=`)
  - Delimiters: `(`, `)`, `{`, `}`, `[`, `]`, `;`, `,`
- **Comment Stripper**: Preserves line numbers when stripping comments (`//` and `/* ... */`).
- **Symbol Table**: Tracks identifier name, symbol type, and first occurrence line number.

## Usage
```bash
python lexical_analyzer.py sample_input.txt
```
