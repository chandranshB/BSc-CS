# Practical 05: LR(0) Parser

## Objective
To construct the canonical collection of LR(0) items, the DFA state transition graph, and the LR(0) Parsing Table (ACTION and GOTO), reporting any Shift/Reduce or Reduce/Reduce conflicts.

## Methodology
1. **Augmented Grammar**: Add $S' \to S$.
2. **Item Construction**: Item is a production with a dot `.` indicating position of scanning ($A \to \alpha . \beta$).
3. **CLOSURE & GOTO Operations**: Computes the set of items reachable from initial item $[S' \to . S]$.
4. **Parsing Action**:
   - Shift on terminals where dot precedes a terminal.
   - Reduce across ALL terminals + `$` for completed items $[A \to \alpha .]$.
   - Report conflicts if an entry has multiple actions.

## Usage
```bash
python lr0_parser.py sample_grammar.txt "( ( a ) )"
```
