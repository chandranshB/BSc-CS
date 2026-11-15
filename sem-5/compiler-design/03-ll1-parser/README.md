# Practical 03: LL(1) Parser

## Objective
To construct an LL(1) predictive parsing table from FIRST and FOLLOW sets, verify that the grammar has no parsing conflicts, and simulate parsing of an input string with a step-by-step stack trace.

## LL(1) Table Construction Rules
For each production $A \to \alpha$:
1. For every terminal $a \in \text{FIRST}(\alpha)$, set $M[A, a] = A \to \alpha$.
2. If $\epsilon \in \text{FIRST}(\alpha)$, for every terminal $b \in \text{FOLLOW}(A)$ (including `$`): set $M[A, b] = A \to \alpha$.
3. If any entry $M[A, a]$ receives multiple productions, report an LL(1) conflict.

## Usage
```bash
python ll1_parser.py sample_grammar.txt "id + id * id"
```
