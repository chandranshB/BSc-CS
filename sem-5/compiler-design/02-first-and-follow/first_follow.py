# ==============================================================================
# Practical 02: FIRST and FOLLOW Set Computation
# Simple recursive calculation of FIRST and FOLLOW for a context-free grammar
# ==============================================================================

import sys

# Grammar stored as a dictionary: Non-terminal -> list of productions
# '#' represents epsilon (null)
grammar = {}
non_terminals = []
terminals = []
start_symbol = None

first = {}
follow = {}


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

    # Find all terminals
    terms = set()
    for lhs, prods in grammar.items():
        for prod in prods:
            for symbol in prod:
                if symbol not in non_terminals and symbol != "#":
                    terms.add(symbol)
    terminals = sorted(list(terms))


def find_first(symbol):
    """Recursive function to find FIRST set of a symbol."""
    # Base case: if it's a terminal or epsilon, FIRST is the symbol itself
    if symbol in terminals or symbol == "#":
        return {symbol}

    # If it's a non-terminal, look at all its productions
    res = set()
    for prod in grammar.get(symbol, []):
        for sym in prod:
            sym_first = find_first(sym)
            # Add all non-epsilon symbols
            res.update(sym_first - {"#"})

            # If epsilon is not in FIRST of this symbol, stop moving forward
            if "#" not in sym_first:
                break
        else:
            # If all symbols in the production derive epsilon, add epsilon
            res.add("#")

    return res


def compute_all_first():
    global first
    first = {}
    for nt in non_terminals:
        first[nt] = find_first(nt)


def compute_all_follow():
    global follow
    follow = {nt: set() for nt in non_terminals}

    # Rule 1: Put $ in FOLLOW of start symbol
    follow[start_symbol].add("$")

    # Repeat until no new symbols can be added to any FOLLOW set
    changed = True
    while changed:
        changed = False
        for lhs, prods in grammar.items():
            for prod in prods:
                n = len(prod)
                for i in range(n):
                    curr = prod[i]
                    if curr in non_terminals:
                        before_len = len(follow[curr])

                        # Look at the rest of the symbols after curr: prod[i+1:]
                        rest = prod[i + 1:]
                        if rest:
                            # Find FIRST of the rest
                            rest_first = set()
                            for s in rest:
                                sf = find_first(s)
                                rest_first.update(sf - {"#"})
                                if "#" not in sf:
                                    break
                            else:
                                # If all rest can be epsilon, add FOLLOW(lhs)
                                rest_first.update(follow[lhs])

                            follow[curr].update(rest_first)
                        else:
                            # Nothing comes after curr, so add FOLLOW(lhs)
                            follow[curr].update(follow[lhs])

                        if len(follow[curr]) > before_len:
                            changed = True


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
    compute_all_first()
    compute_all_follow()

    print("-" * 55)
    print("               FIRST AND FOLLOW SETS")
    print("-" * 55)
    print(f"{'Non-Terminal':<16}{'FIRST':<22}{'FOLLOW'}")
    print("-" * 55)
    for nt in non_terminals:
        first_str = "{ " + ", ".join(sorted(first[nt])) + " }"
        follow_str = "{ " + ", ".join(sorted(follow[nt])) + " }"
        print(f"{nt:<16}{first_str:<22}{follow_str}")
    print("-" * 55)


if __name__ == "__main__":
    main()
