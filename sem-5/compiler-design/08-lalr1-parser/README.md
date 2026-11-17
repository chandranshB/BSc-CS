# Practical 08: LALR(1) Parser (Look-Ahead LR)

## Objective
To implement an LALR(1) parser by generating the canonical LR(1) states, grouping and merging states with identical LR(0) cores, building the compact LALR(1) parsing table, and parsing input strings.

## Merging Mechanism
- Core of state $I = \{(A \to \alpha . \beta) \mid [A \to \alpha . \beta, a] \in I\}$.
- States with the exact same cores are merged:
  - e.g., State 4 and State 7 merge into $I_{4\_7}$
  - Lookaheads for identical core items are combined via set union.
- Reduces the state space (e.g., from 10 CLR states down to 7 LALR states) while retaining parsing power.

## Usage
```bash
python lalr1_parser.py sample_grammar.txt "c c d d"
```
