# C Programming Practice

A collection of beginner-to-intermediate C programs organized by concept —
conditionals, switch statements, and loops. Each file is self-contained,
cleanly written, and ready to compile.

---

## Structure

| Range | Topic |
|-------|-------|
| `question-01` → `question-25` | If / Else — decision making |
| `question-26` → `question-47` | Switch — branching with style |
| `question-47` → `question-64` | Loops — iteration and series |

---

## If / Else  `question-01 to question-25`

| # | What it does |
|---|--------------|
| 01 | Check if a number is positive, negative, or zero |
| 02 | Find a student's grade based on marks in 5 subjects |
| 03 | Find the greatest of two numbers |
| 04 | Find the largest of three numbers |
| 05 | Check if a character is a vowel or consonant |
| 06 | Check if a character is an alphabet |
| 07 | Classify a character — lowercase, uppercase, digit, or special |
| 08 | Find the absolute value of a number |
| 09 | Check divisibility by both 5 and 11 |
| 10 | Grade calculator using switch-style percentage bands |
| 11 | Voting eligibility check |
| 12 | Driving eligibility check |
| 13 | Find the youngest among 3 people |
| 14 | Find the oldest among 3 people |
| 15 | Validate a triangle by its angles |
| 16 | Classify a triangle — equilateral, isosceles, or scalene |
| 17 | Check if a number is an Armstrong number |
| 18 | Check divisibility by both 3 and 7 |
| 19 | Check if a year is a leap year |
| 20 | Check if a number is prime |
| 21 | Find roots of a quadratic equation (real or complex) |
| 22 | Calculate profit or loss percentage |
| 23 | Check if a number is a palindrome |
| 24 | Check if a number is a perfect square |
| 25 | Calculate electricity bill based on slab rates |

---

## Switch  `question-26 to question-47`

| # | What it does |
|---|--------------|
| 26 | Simple calculator (+, −, ×, ÷) |
| 27 | Find the maximum of two numbers |
| 28 | Find the maximum of three numbers (nested switch) |
| 29 | Print the day of the week from a number |
| 30 | Print the month name from a number |
| 31 | Find the number of days in a given month (leap year aware) |
| 32 | Check if a character is a vowel or consonant |
| 33 | Classify a character — alphabet, digit, or special symbol |
| 34 | Menu-driven area calculator (circle, rectangle, triangle) |
| 35 | Menu-driven volume calculator (cube, cuboid, sphere) |
| 36 | Check if a number is even or odd |
| 37 | Display grade from marks |
| 38 | Print multiplication table |
| 39 | Unit conversion — distance (km, m, cm) |
| 40 | Temperature conversion (Celsius ↔ Fahrenheit) |
| 41 | Simple and compound interest calculator |
| 42 | Triangle type checker with validity check |
| 43 | Pattern printer (square, triangle, pyramid) |
| 44 | Math menu — factorial, Fibonacci, prime check |
| 45 | Reverse a string or a number |
| 46 | Matrix addition and subtraction |
| 47 | ATM simulation (exit-controlled menu) |

---

## Loops  `question-47 to question-64`

| # | What it does |
|---|--------------|
| 47 | Print numbers 1 to 10 |
| 48 | Print numbers 10 to 1 |
| 49 | Print even numbers from 1 to 100 |
| 50 | Print odd numbers from 1 to 100 |
| 51 | Print multiplication table of a given number |
| 52 | Find the reverse of a number |
| 53 | Count the digits in a number |
| 54 | Find the sum of digits |
| 55 | Find the product of digits |
| 56 | Check if a number is a palindrome |
| 57 | Check if a number is an Armstrong number |
| 58 | Check if a number is a perfect number |
| 59 | Check if a number is prime |
| 60 | Print all prime numbers in a range |
| 61 | Print Fibonacci series up to N terms |
| 62 | Print Fibonacci series and its sum |
| 63 | Print Arithmetic Progression (A.P.) series |
| 64 | Print Geometric Progression (G.P.) series |

---

## How to compile

Any standard C compiler works. With GCC:

```bash
gcc question-01.c -o q01 && ./q01
```

For programs using `math.h` (questions 20, 21, 24, 33, 34, 40, 43, 59, 60):

```bash
gcc question-20.c -o q20 -lm && ./q20
```

---

## Notes

- All programs use `int main()` with `return 0` — fully standard C99/C11 compliant.
- `clrscr()` and `getch()` have been removed (those are Turbo C relics that don't belong in modern C).
- Several bugs were quietly fixed along the way — wrong comparisons, undefined variables, missing semicolons, misplaced braces. The logic is now correct.
- Every file has a comment at the top describing what it does, so you never have to guess.
