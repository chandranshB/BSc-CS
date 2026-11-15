# ==============================================================================
# Practical 03: LL(1) Parser
# Simple predictive LL(1) parsing table construction and string parsing
# ==============================================================================

import sys

grammar = {}
non_terminals = []
terminals = []
start_symbol = None

first = {}
follow = {}
table = {}


def load_grammar(text):
    global grammar, non_terminals, terminals, start_symbol
    grammar = {}
    non_terminals = []

    lines = [line.strip() for line in text.strip().split("\n") if line.strip() and not line.strip().startswith("//")]
    for line in lines:
        lhs, rhs = line.split("->")
        lhs = lhs.strip()
        if lhs not in non_terminals:
            non_terminals.append(lhs)
        if start_symbol is None:
            start_symbol = lhs

        alts = [alt.strip().split() for alt in rhs.split("|")]
        grammar[lhs] = alts

    terms = set()
    for lhs, prods in grammar.items():
        for prod in prods:
            for s in prod:
                if s not in non_terminals and s != "#":
                    terms.add(s)
    terminals = sorted(list(terms))


def find_first(symbol):
    if symbol in terminals or symbol == "#":
        return {symbol}

    res = set()
    for prod in grammar.get(symbol, []):
        for sym in prod:
            sym_first = find_first(sym)
            res.update(sym_first - {"#"})
            if "#" not in sym_first:
                break
        else:
            res.add("#")
    return res


def compute_first_and_follow():
    global first, follow
    first = {nt: find_first(nt) for nt in non_terminals}
    follow = {nt: set() for nt in non_terminals}
    follow[start_symbol].add("$")

    changed = True
    while changed:
        changed = False
        for lhs, prods in grammar.items():
            for prod in prods:
                for i in range(len(prod)):
                    curr = prod[i]
                    if curr in non_terminals:
                        before = len(follow[curr])
                        rest = prod[i + 1:]
                        if rest:
                            rest_first = set()
                            for s in rest:
                                sf = find_first(s)
                                rest_first.update(sf - {"#"})
                                if "#" not in sf:
                                    break
                            else:
                                rest_first.update(follow[lhs])
                            follow[curr].update(rest_first)
                        else:
                            follow[curr].update(follow[lhs])

                        if len(follow[curr]) > before:
                            changed = True


def build_ll1_table():
    global table
    cols = terminals + ["$"]
    table = {nt: {t: None for t in cols} for nt in non_terminals}

    for lhs, prods in grammar.items():
        for prod in prods:
            prod_str = f"{lhs} -> {' '.join(prod)}"

            # Find FIRST of the production body
            body_first = set()
            for sym in prod:
                sf = find_first(sym)
                body_first.update(sf - {"#"})
                if "#" not in sf:
                    break
            else:
                body_first.add("#")

            # Place production in table for each terminal in FIRST(body)
            for t in body_first - {"#"}:
                table[lhs][t] = prod_str

            # If epsilon is in FIRST(body), place in table for terminals in FOLLOW(lhs)
            if "#" in body_first:
                for t in follow[lhs]:
                    table[lhs][t] = prod_str


def print_table():
    print("-" * 65)
    print("                    LL(1) PARSING TABLE")
    print("-" * 65)
    cols = terminals + ["$"]
    header = f"{'Non-Term':<10}" + "".join(f"{c:<16}" for c in cols)
    print(header)
    print("-" * len(header))
    for nt in non_terminals:
        row = f"{nt:<10}"
        for c in cols:
            val = table[nt][c] or "---"
            row += f"{val:<16}"
        print(row)
    print("-" * len(header))


def parse_string(tokens):
    print("\n" + "=" * 65)
    print(f"Parsing Input: {' '.join(tokens)}")
    print("=" * 65)
    print(f"{'Step':<6}{'Stack':<24}{'Input Buffer':<18}{'Action'}")
    print("-" * 65)

    stack = ["$", start_symbol]
    buffer = list(tokens) + ["$"]
    step = 1

    while len(stack) > 0:
        top = stack[-1]
        curr = buffer[0]

        stack_str = " ".join(stack)
        buf_str = " ".join(buffer)

        # Successful parsing condition
        if top == "$" and curr == "$":
            print(f"{step:<6}{stack_str:<24}{buf_str:<18}ACCEPT (Parsed Successfully)")
            return True

        # Match terminal on top of stack with current input symbol
        if top == curr:
            print(f"{step:<6}{stack_str:<24}{buf_str:<18}Match '{curr}'")
            stack.pop()
            buffer.pop(0)
        elif top in terminals or top == "$":
            print(f"{step:<6}{stack_str:<24}{buf_str:<18}ERROR: Unexpected symbol '{curr}'")
            return False
        else:
            # Expand non-terminal from LL(1) table
            rule = table[top].get(curr)
            if rule is None:
                print(f"{step:<6}{stack_str:<24}{buf_str:<18}ERROR: No rule for [{top}, {curr}]")
                return False

            print(f"{step:<6}{stack_str:<24}{buf_str:<18}Apply {rule}")
            stack.pop()
            rhs = rule.split("->")[1].strip().split()
            # Push in reverse order (ignore epsilon '#')
            if rhs != ["#"]:
                for s in reversed(rhs):
                    stack.append(s)

        step += 1

    return False


def main():
    default_grammar = """
    E -> T E'
    E' -> + T E' | #
    T -> F T'
    T' -> * F T' | #
    F -> ( E ) | id
    """

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    else:
        text = default_grammar

    load_grammar(text)
    compute_first_and_follow()
    build_ll1_table()
    print_table()

    # Input string to test
    input_str = ["id", "+", "id", "*", "id"]
    if len(sys.argv) > 2:
        input_str = sys.argv[2].split()

    parse_string(input_str)


if __name__ == "__main__":
    main()
