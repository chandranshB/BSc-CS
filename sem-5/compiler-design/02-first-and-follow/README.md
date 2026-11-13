# Practical 02: FIRST and FOLLOW Set Computation

## Objective
To compute the `FIRST` and `FOLLOW` sets for any given Context-Free Grammar (CFG).

## Algorithm
1. **FIRST Set**:
   - If $X$ is a terminal, $\text{FIRST}(X) = \{X\}$.
   - If $X \to \epsilon$, add $\epsilon$ to $\text{FIRST}(X)$.
   - If $X \to Y_1 Y_2 \dots Y_k$, add non-$\epsilon$ symbols of $\text{FIRST}(Y_1)$ to $\text{FIRST}(X)$. If $Y_1 \Rightarrow^* \epsilon$, continue to $Y_2$, and so forth. If all $Y_i \Rightarrow^* \epsilon$, add $\epsilon$.
   - Iterate using fixed-point iteration until no new symbols are added.
2. **FOLLOW Set**:
   - Place `$` in $\text{FOLLOW}(S)$ where $S$ is the start symbol.
   - If $A \to \alpha B \beta$, add $\text{FIRST}(\beta) \setminus \{\epsilon\}$ to $\text{FOLLOW}(B)$.
   - If $A \to \alpha B$ or $A \to \alpha B \beta$ where $\epsilon \in \text{FIRST}(\beta)$, add $\text{FOLLOW}(A)$ to $\text{FOLLOW}(B)$.

## Usage
```bash
python first_follow.py sample_grammar.txt
```
