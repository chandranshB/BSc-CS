# Practical 06: SLR(1) Parser (Simple LR)

## Objective
To build an SLR(1) parser using LR(0) canonical items, utilizing the FOLLOW set of non-terminals to resolve reduce actions and eliminate LR(0) shift/reduce conflicts.

## Table Construction Rule
For each state $I_i$:
1. If $[A \to \alpha . a \beta] \in I_i$ and $\text{GOTO}(I_i, a) = I_j$, set $\text{ACTION}[i, a] = \text{shift } j$.
2. If $[A \to \alpha .] \in I_i$, set $\text{ACTION}[i, a] = \text{reduce } k$ ONLY for $a \in \text{FOLLOW}(A)$.
3. If $[S' \to S .] \in I_i$, set $\text{ACTION}[i, \$] = \text{accept}$.
4. If $\text{GOTO}(I_i, A) = I_j$, set $\text{GOTO}[i, A] = j$.

## Usage
```bash
python slr1_parser.py sample_grammar.txt "id + id * id"
```
