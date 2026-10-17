# BSc-CS

Practical coursework and assignments for Bachelor of Science in Computer Science.

## Repository Layout

```
BSc-CS/
├── sem-1 (C)/
│   └── (C programming coursework)
└── sem-2 (python)/
    ├── mid-sem/
    │   ├── 01. Vowel Count in input.py
    │   ├── 02. Even Counter in list.py
    │   ├── 03. Palindrome number Checker.py
    │   └── ... (30 fundamental practice scripts)
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

### Semester 2: Python

#### Mid-Sem (`sem-2 (python)/mid-sem/`)
Thirty foundational Python programs covering:
- Strings: vowel counting, reversals, spammer, string length, word count, case identification
- Numbers and math: palindrome checks, Armstrong numbers, factorial, Fibonacci series, prime checks, even/odd filters
- Data structures: list operations, tuple uniqueness and element sums, set operations and multipliers, dictionary iterations and key filtering

#### End-Sem (`sem-2 (python)/end-sem/`)
End-semester practical work covering modular programming, custom package structure, and exception handling:
- `cal1.py`: Arithmetic module providing add, sub, mul, div, mod, and pow functions.
- `list1.py`, `dict3.py`, `set2.py`: Custom utility modules implementing common data structure operations.
- `mypackage/`: Custom Python package re-exporting list, set, and dictionary operations through `__init__.py`.
- `m4.py`, `m5.py`, `m6.py`: Driver scripts demonstrating module imports, calculator operations, and package imports.
- `exceptions.py`: Demonstration of handling Python built-in exceptions (`ZeroDivisionError`, `NameError`, `KeyError`, `IndexError`, `ValueError`, `AttributeError`, `FileNotFoundError`, `ModuleNotFoundError`, and generic `Exception`).

## Running the Code

### Mid-Sem Programs
Run any script directly using Python 3:

```bash
python "sem-2 (python)/mid-sem/01. Vowel Count in input.py"
```

### End-Sem Programs
To execute the driver scripts, run from within the `end-sem` directory so local modules and `mypackage` are resolved:

```bash
cd "sem-2 (python)/end-sem"
python m4.py
python m5.py
python m6.py
python exceptions.py
```
