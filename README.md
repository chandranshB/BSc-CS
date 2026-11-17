# BSc-CS

Practical coursework, lab assignments, and programs for Bachelor of Science in Computer Science.

## Repository Layout

```
BSc-CS/
├── sem-1 (C)/
│   ├── question-01.c to question-25.c       (Conditionals)
│   ├── question-26-switch.c to 47-switch.c  (Switch Statements)
│   ├── question-47-loops.c to 64-loops.c    (Loops and Series)
│   └── README.md
├── sem-2 (python)/
│   ├── mid-sem/
│   │   ├── 01. Vowel Count in input.py
│   │   ├── 02. Even Counter in list.py
│   │   ├── 03. Palindrome number Checker.py
│   │   └── ... (30 foundational practice scripts)
│   └── end-sem/
│       ├── mypackage/
│       │   ├── __init__.py
│       │   ├── dict3.py
│       │   ├── list1.py
│       │   └── set2.py
│       ├── cal1.py
│       ├── dict3.py
│       ├── exceptions.py
│       ├── list1.py
│       ├── m4.py
│       ├── m5.py
│       ├── m6.py
│       └── set2.py
└── sem-5/
    └── compiler-design/
        ├── 01-lexical-analyzer/
        ├── 02-first-and-follow/
        ├── 03-ll1-parser/
        ├── 04-operator-precedence-parser/
        ├── 05-lr0-parser/
        ├── 06-slr1-parser/
        ├── 07-clr1-parser/
        ├── 08-lalr1-parser/
        └── README.md
```

## Contents

### Semester 1: C Programming (`sem-1 (C)/`)
64 standalone programs organized by core language constructs:
- Conditionals (`question-01.c` to `question-25.c`): Positivity checks, grade evaluation, largest/smallest of numbers, character classification, triangle validation, Armstrong numbers, leap years, primes, quadratic roots, and profit/loss calculation.
- Switch statements (`question-26-switch.c` to `question-47-switch.c`): Basic calculator, day and month lookup, area and volume menus, unit and temperature conversions, pattern generators, matrix addition/subtraction, and an ATM console simulation.
- Loops (`question-47-loops.c` to `question-64-loops.c`): Forward and reverse number printing, even/odd ranges, digit extraction and summation, product of digits, palindromes, prime ranges, Fibonacci series, and arithmetic/geometric progression generators.

### Semester 2: Python (`sem-2 (python)/`)

#### Mid-Sem (`sem-2 (python)/mid-sem/`)
Thirty foundational Python programs covering:
- Strings: vowel counting, reversals, repetition, character count, word count, and uppercase/lowercase identification.
- Numbers and math: palindrome checks, Armstrong numbers, factorial calculation, Fibonacci series, prime checks, and parity filters.
- Collections: list manipulations, tuple uniqueness and element sums, set operations and multipliers, dictionary iterations, and key filtering.

#### End-Sem (`sem-2 (python)/end-sem/`)
Modular programs, custom package architecture, and structured exception handling:
- `cal1.py`: Arithmetic module providing `add1`, `sub1`, `mul1`, `div1`, `mod1`, and `pow1`.
- `list1.py`, `dict3.py`, `set2.py`: Utility modules implementing operations for lists, dictionaries, and sets.
- `mypackage/`: Custom Python package exporting collection helper functions via `__init__.py`.
- `m4.py`, `m5.py`, `m6.py`: Driver scripts demonstrating module imports, arithmetic operations, and package consumption.
- `exceptions.py`: Comprehensive reference for handling standard Python exceptions (`ZeroDivisionError`, `NameError`, `KeyError`, `IndexError`, `ValueError`, `AttributeError`, `FileNotFoundError`, `ModuleNotFoundError`, and generic `Exception`).

### Semester 5: Compiler Design (`sem-5/compiler-design/`)
Beginner-friendly, clean implementations of core compiler front-end practicals:
1. `01-lexical-analyzer/`: Lexical scanner identifying keywords, identifiers, constants, literals, operators, and delimiters with comment stripping and symbol table generation.
2. `02-first-and-follow/`: Computation of `FIRST` and `FOLLOW` sets for arbitrary context-free grammars with $\epsilon$ handling.
3. `03-ll1-parser/`: Predictive LL(1) parse table construction and input string parsing with stack trace.
4. `04-operator-precedence-parser/`: Operator precedence relation matrix (`<`, `=`, `>`) generation and shift-reduce parsing.
5. `05-lr0-parser/`: Canonical collection of LR(0) items, DFA transitions, and ACTION/GOTO parsing table construction.
6. `06-slr1-parser/`: Simple LR parser resolving reduce actions via `FOLLOW` sets to eliminate conflicts.
7. `07-clr1-parser/`: Canonical LR(1) parser with lookaheads $[A \to \alpha . \beta, a]$ and parsing simulation.
8. `08-lalr1-parser/`: Look-Ahead LR parser merging states with identical LR(0) cores with parsing simulation.

## Running the Code

### C Programs
Compile using any standard C compiler (such as GCC):

```bash
cd "sem-1 (C)"
gcc question-01.c -o q01 && ./q01
```

For programs using `math.h` (questions 20, 21, 24, 33, 34, 40, 43, 59, 60), link the math library:

```bash
gcc question-20.c -o q20 -lm && ./q20
```

### Python Programs

#### Mid-Sem
Run any script directly using Python 3:

```bash
python "sem-2 (python)/mid-sem/01. Vowel Count in input.py"
```

#### End-Sem
Run driver scripts from within the `end-sem` directory so local modules and `mypackage` are discovered:

```bash
cd "sem-2 (python)/end-sem"
python m4.py
python m5.py
python m6.py
python exceptions.py
```

### Compiler Design Practicals (Semester 5)
Run any practical directly with Python 3:

```bash
cd "sem-5/compiler-design"

# Practical 01: Lexical Analysis
python 01-lexical-analyzer/lexical_analyzer.py 01-lexical-analyzer/sample_input.txt

# Practical 02: FIRST & FOLLOW
python 02-first-and-follow/first_follow.py 02-first-and-follow/sample_grammar.txt

# Practical 03: LL(1) Parser
python 03-ll1-parser/ll1_parser.py 03-ll1-parser/sample_grammar.txt "id + id * id"

# Practical 04: Operator Precedence Parser
python 04-operator-precedence-parser/operator_precedence_parser.py "id + id * id"

# Practical 05: LR(0) Parser
python 05-lr0-parser/lr0_parser.py 05-lr0-parser/sample_grammar.txt "( ( a ) )"

# Practical 06: SLR(1) Parser
python 06-slr1-parser/slr1_parser.py 06-slr1-parser/sample_grammar.txt "id + id * id"

# Practical 07: CLR(1) Parser
python 07-clr1-parser/clr1_parser.py 07-clr1-parser/sample_grammar.txt "c c d d"

# Practical 08: LALR(1) Parser
python 08-lalr1-parser/lalr1_parser.py 08-lalr1-parser/sample_grammar.txt "c c d d"
```
