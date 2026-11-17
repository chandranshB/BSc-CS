# Compiler Design Lab Practicals 🚀

A comprehensive, modular, and academic-grade collection of **Compiler Design Practical Experiments** implemented in **Python 3**. Each experiment is self-contained with its own source code, sample inputs, sample execution logs, and detailed algorithm notes.

Zero external dependencies are required—all programs use standard Python libraries (`sys`, `re`, `collections`).

---

## 📚 Table of Contents

| # | Practical Topic | Directory | Key Concepts |
|---|-----------------|-----------|--------------|
| 01 | **Lexical Analysis (Scanner)** | [`01-lexical-analyzer/`](./01-lexical-analyzer/) | Tokenization, Comment Stripping, Symbol Table, Lexical Errors |
| 02 | **FIRST & FOLLOW Sets** | [`02-first-and-follow/`](./02-first-and-follow/) | Context-Free Grammar, Fixed-Point Iteration, Nullable / Epsilon |
| 03 | **LL(1) Parser** | [`03-ll1-parser/`](./03-ll1-parser/) | Predictive Parsing Table, LL(1) Conflict Detection, Stack Trace |
| 04 | **Operator Precedence Parser** | [`04-operator-precedence-parser/`](./04-operator-precedence-parser/) | Precedence Matrix (`<.`, `=.`, `.>`), Handle Pruning, Shift-Reduce |
| 05 | **LR(0) Parser** | [`05-lr0-parser/`](./05-lr0-parser/) | Augmented Grammar, LR(0) Items, Item Closure & GOTO, Conflict Checking |
| 06 | **SLR(1) Parser** | [`06-slr1-parser/`](./06-slr1-parser/) | LR(0) Automaton + FOLLOW Set Reductions, Ambiguity Resolution |
| 07 | **CLR(1) Parser** | [`07-clr1-parser/`](./07-clr1-parser/) | Canonical LR(1) Items `[A -> α . β, a]`, Lookahead Propagation, DFA |
| 08 | **LALR(1) Parser** | [`08-lalr1-parser/`](./08-lalr1-parser/) | LR(0) Core Merging, Lookahead Union, State Reduction (10 -> 7) |

---

## 🛠️ Prerequisites & Setup

- **Python Version**: Python 3.7 or higher
- **Installation**: No external pip packages needed!

Verify your Python installation:
```bash
python --version
```

---

## 🚀 How to Run Each Practical

You can run each practical either with its built-in sample data or by passing custom input grammar/code files.

### 1. Lexical Analysis
```bash
# Run with sample C source file
python 01-lexical-analyzer/lexical_analyzer.py 01-lexical-analyzer/sample_input.txt

# Or run interactively with built-in code
python 01-lexical-analyzer/lexical_analyzer.py
```

### 2. FIRST and FOLLOW
```bash
# Run with sample CFG
python 02-first-and-follow/first_follow.py 02-first-and-follow/sample_grammar.txt
```

### 3. LL(1) Parser
```bash
# Run with sample CFG and custom input string
python 03-ll1-parser/ll1_parser.py 03-ll1-parser/sample_grammar.txt "id + id * id"
```

### 4. Operator Precedence Parser
```bash
# Run with expression string
python 04-operator-precedence-parser/operator_precedence_parser.py "id + id * id"
```

### 5. LR(0) Parser
```bash
# Run with parenthesis grammar and token sequence
python 05-lr0-parser/lr0_parser.py 05-lr0-parser/sample_grammar.txt "( ( a ) )"
```

### 6. SLR(1) Parser
```bash
# Run with arithmetic expression grammar and token sequence
python 06-slr1-parser/slr1_parser.py 06-slr1-parser/sample_grammar.txt "id + id * id"
```

### 7. CLR(1) Parser
```bash
# Run with classic Dragon Book CLR grammar
python 07-clr1-parser/clr1_parser.py 07-clr1-parser/sample_grammar.txt "c c d d"
```

### 8. LALR(1) Parser
```bash
# Run with core-merging grammar
python 08-lalr1-parser/lalr1_parser.py 08-lalr1-parser/sample_grammar.txt "c c d d"
```

---

## 📁 Repository Structure

```
compiler-design-lab/
├── README.md
├── 01-lexical-analyzer/
│   ├── lexical_analyzer.py
│   ├── sample_input.txt
│   ├── sample_output.txt
│   └── README.md
├── 02-first-and-follow/
│   ├── first_follow.py
│   ├── sample_grammar.txt
│   ├── sample_output.txt
│   └── README.md
├── 03-ll1-parser/
│   ├── ll1_parser.py
│   ├── sample_grammar.txt
│   ├── sample_output.txt
│   └── README.md
├── 04-operator-precedence-parser/
│   ├── operator_precedence_parser.py
│   ├── sample_input.txt
│   ├── sample_output.txt
│   └── README.md
├── 05-lr0-parser/
│   ├── lr0_parser.py
│   ├── sample_grammar.txt
│   ├── sample_output.txt
│   └── README.md
├── 06-slr1-parser/
│   ├── slr1_parser.py
│   ├── sample_grammar.txt
│   ├── sample_output.txt
│   └── README.md
├── 07-clr1-parser/
│   ├── clr1_parser.py
│   ├── sample_grammar.txt
│   ├── sample_output.txt
│   └── README.md
└── 08-lalr1-parser/
    ├── lalr1_parser.py
    ├── sample_grammar.txt
    ├── sample_output.txt
    └── README.md
```

---

## 📌 Note on Commits
The repository is initialized locally. When ready to commit and push to GitHub, run:
```bash
git add .
git commit -m "Add compiler design lab practical implementations (Practicals 01 to 08)"
git remote add origin <YOUR_GITHUB_REPO_URL>
git branch -M main
git push -u origin main
```
