# Compiler Design Lab

Compiler Design practicals implemented in Python.

## Practicals

1. Lexical Analyzer - Tokenize C source code and print tokens and symbol table.
2. FIRST and FOLLOW - Calculate FIRST and FOLLOW sets for a context-free grammar.
3. LL(1) Parser - Predictive parsing table construction and input string parsing.
4. Operator Precedence Parser - Shift-reduce parsing using an operator precedence matrix.
5. LR(0) Parser - LR(0) canonical items, table construction, and parsing.
6. SLR(1) Parser - Simple LR parsing using FOLLOW sets for reduce actions.
7. CLR(1) Parser - Canonical LR(1) parser with lookaheads.
8. LALR(1) Parser - LALR(1) parser with merged LR(0) cores.

## How to Run

Run any script with Python 3:

```bash
# Practical 1: Lexical Analysis
python 01-lexical-analyzer/lexical_analyzer.py 01-lexical-analyzer/sample_input.txt

# Practical 2: FIRST and FOLLOW
python 02-first-and-follow/first_follow.py 02-first-and-follow/sample_grammar.txt

# Practical 3: LL(1) Parser
python 03-ll1-parser/ll1_parser.py 03-ll1-parser/sample_grammar.txt "id + id * id"

# Practical 4: Operator Precedence Parser
python 04-operator-precedence-parser/operator_precedence_parser.py "id + id * id"

# Practical 5: LR(0) Parser
python 05-lr0-parser/lr0_parser.py 05-lr0-parser/sample_grammar.txt "( ( a ) )"

# Practical 6: SLR(1) Parser
python 06-slr1-parser/slr1_parser.py 06-slr1-parser/sample_grammar.txt "id + id * id"

# Practical 7: CLR(1) Parser
python 07-clr1-parser/clr1_parser.py 07-clr1-parser/sample_grammar.txt "c c d d"

# Practical 8: LALR(1) Parser
python 08-lalr1-parser/lalr1_parser.py 08-lalr1-parser/sample_grammar.txt "c c d d"
```
