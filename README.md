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
└── sem-2 (python)/
    ├── mid-sem/
    │   ├── 01. Vowel Count in input.py
    │   ├── 02. Even Counter in list.py
    │   ├── 03. Palindrome number Checker.py
    │   └── ... (30 foundational practice scripts)
    └── end-sem/
        ├── mypackage/
        │   ├── __init__.py
        │   ├── dict3.py
        │   ├── list1.py
        │   └── set2.py
        ├── cal1.py
        ├── dict3.py
        ├── exceptions.py
        ├── list1.py
        ├── m4.py
        ├── m5.py
        ├── m6.py
        └── set2.py
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
