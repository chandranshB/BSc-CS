# Practical 07: CLR(1) Parser (Canonical LR)

## Objective
To construct the canonical collection of LR(1) items $[A \to \alpha . \beta, a]$ with explicit lookahead terminals, construct the CLR(1) parsing table, and parse input tokens.

## LR(1) Closure Rule
If $[A \to \alpha . B \beta, a] \in I$:
- For each production $B \to \gamma$ and each terminal $b \in \text{FIRST}(\beta a)$, add $[B \to . \gamma, b]$ to the closure.

## Usage
```bash
python clr1_parser.py sample_grammar.txt "c c d d"
```
