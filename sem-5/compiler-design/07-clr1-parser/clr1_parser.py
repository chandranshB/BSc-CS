# ==============================================================================
# Practical 07: CLR(1) Parser (Canonical LR)
# Simple LR(1) item generation [A -> alpha . beta, lookahead] and parsing table
# ==============================================================================

import sys

productions = []  # (head, [symbols])
non_terminals = []
terminals = []
start_symbol = None

states = []  # list of sets of items: (prod_idx, dot_pos, lookahead)
transitions = {}  # (state_idx, symbol) -> next_state_idx
action_table = {}
goto_table = {}


def load_grammar(text):
    global productions, non_terminals, terminals, start_symbol
    productions = []
    non_terminals = []

    lines = [l.strip() for l in text.strip().split("\n") if l.strip() and not l.strip().startswith("//")]
    for line in lines:
        lhs, rhs = line.split("->")
        lhs = lhs.strip()
        if lhs not in non_terminals:
            non_terminals.append(lhs)
        if start_symbol is None:
            start_symbol = lhs

        for alt in rhs.split("|"):
            symbols = alt.strip().split()
            productions.append((lhs, symbols))

    # Augmented production S' -> S
    aug_start = start_symbol + "'"
    productions.insert(0, (aug_start, [start_symbol]))
    non_terminals.insert(0, aug_start)

    terms = set()
    for head, body in productions:
        for s in body:
            if s not in non_terminals:
                terms.add(s)
    terminals = sorted(list(terms))


def find_first_of_sequence(seq):
    """Find FIRST of a sequence of symbols."""
    res = set()
    for s in seq:
        if s in terminals or s == "$":
            res.add(s)
            break
        elif s in non_terminals:
            # find first of this non-terminal
            s_first = set()
            for head, body in productions:
                if head == s:
                    for b in body:
                        if b in terminals:
                            s_first.add(b)
                            break
                        elif b == "#":
                            s_first.add("#")
                            break
            res.update(s_first - {"#"})
            if "#" not in s_first:
                break
    else:
        res.add("#")
    return res


def lr1_closure(items):
    """Compute LR(1) closure for items (prod_idx, dot, lookahead)."""
    current_set = set(items)
    changed = True
    while changed:
        changed = False
        new_items = set()
        for prod_idx, dot, la in current_set:
            head, body = productions[prod_idx]
            if dot < len(body):
                sym = body[dot]
                if sym in non_terminals:
                    # Lookahead is FIRST of (remaining_symbols + [la])
                    remaining = body[dot + 1:] + [la]
                    las = find_first_of_sequence(remaining)

                    for p_idx, (p_head, p_body) in enumerate(productions):
                        if p_head == sym:
                            for b in las:
                                item = (p_idx, 0, b)
                                if item not in current_set and item not in new_items:
                                    new_items.add(item)
                                    changed = True
        current_set.update(new_items)
    return current_set


def lr1_goto(items, symbol):
    moved = set()
    for prod_idx, dot, la in items:
        head, body = productions[prod_idx]
        if dot < len(body) and body[dot] == symbol:
            moved.add((prod_idx, dot + 1, la))
    return lr1_closure(moved) if moved else set()


def build_clr1_states():
    global states, transitions
    # Initial item [S' -> . S, $]
    i0 = lr1_closure([(0, 0, "$")])
    states = [i0]
    transitions = {}

    all_symbols = non_terminals + terminals
    queue = [0]

    while queue:
        curr_idx = queue.pop(0)
        curr_state = states[curr_idx]

        for sym in all_symbols:
            next_st = lr1_goto(curr_state, sym)
            if not next_st:
                continue

            if next_st not in states:
                states.append(next_st)
                new_idx = len(states) - 1
                queue.append(new_idx)
            else:
                new_idx = states.index(next_st)

            transitions[(curr_idx, sym)] = new_idx


def build_clr1_table():
    global action_table, goto_table
    action_cols = terminals + ["$"]
    goto_cols = [nt for nt in non_terminals if nt != productions[0][0]]

    action_table = {i: {t: None for t in action_cols} for i in range(len(states))}
    goto_table = {i: {nt: None for nt in goto_cols} for i in range(len(states))}

    for i, state in enumerate(states):
        for prod_idx, dot, la in state:
            head, body = productions[prod_idx]

            # Shift condition
            if dot < len(body):
                sym = body[dot]
                if sym in terminals and (i, sym) in transitions:
                    next_s = transitions[(i, sym)]
                    action_table[i][sym] = f"s{next_s}"
            else:
                # Reduce condition: place reduce strictly under lookahead terminal
                if prod_idx == 0 and la == "$":
                    action_table[i]["$"] = "acc"
                else:
                    action_table[i][la] = f"r{prod_idx}"

        for nt in goto_cols:
            if (i, nt) in transitions:
                goto_table[i][nt] = transitions[(i, nt)]


def print_table():
    print("-" * 75)
    print("                         CLR(1) PARSING TABLE")
    print("-" * 75)
    action_cols = terminals + ["$"]
    goto_cols = [nt for nt in non_terminals if nt != productions[0][0]]

    header = f"{'State':<7}| " + "".join(f"{a:<7}" for a in action_cols) + "| " + "".join(f"{g:<7}" for g in goto_cols)
    print(header)
    print("-" * len(header))
    for i in range(len(states)):
        row = f"{i:<7}| "
        for a in action_cols:
            val = action_table[i][a] or "-"
            row += f"{val:<7}"
        row += "| "
        for g in goto_cols:
            val = str(goto_table[i][g]) if goto_table[i][g] is not None else "-"
            row += f"{val:<7}"
        print(row)
    print("-" * len(header))


def parse_string(tokens):
    buffer = list(tokens) + ["$"]
    state_stack = [0]
    symbol_stack = ["$"]
    step = 1

    print("\n" + "=" * 75)
    print(f"Parsing Input: {' '.join(tokens)}")
    print("=" * 75)
    print(f"{'Step':<6}{'State Stack':<22}{'Symbol Stack':<18}{'Input':<16}{'Action'}")
    print("-" * 75)

    while True:
        s = state_stack[-1]
        a = buffer[0]
        act = action_table[s].get(a)

        s_str = " ".join(str(x) for x in state_stack)
        sym_str = " ".join(symbol_stack)
        buf_str = " ".join(buffer)

        if act == "acc":
            print(f"{step:<6}{s_str:<22}{sym_str:<18}{buf_str:<16}ACCEPT (Parsed Successfully)")
            return True
        elif act and act.startswith("s"):
            next_s = int(act[1:])
            print(f"{step:<6}{s_str:<22}{sym_str:<18}{buf_str:<16}Shift to state {next_s}")
            symbol_stack.append(a)
            state_stack.append(next_s)
            buffer.pop(0)
        elif act and act.startswith("r"):
            p_idx = int(act[1:])
            head, body = productions[p_idx]
            print(f"{step:<6}{s_str:<22}{sym_str:<18}{buf_str:<16}Reduce by {head} -> {' '.join(body)}")
            for _ in range(len(body)):
                state_stack.pop()
                symbol_stack.pop()
            top_s = state_stack[-1]
            goto_s = goto_table[top_s][head]
            symbol_stack.append(head)
            state_stack.append(goto_s)
        else:
            print(f"{step:<6}{s_str:<22}{sym_str:<18}{buf_str:<16}ERROR: Syntax Error at state {s} with '{a}'")
            return False

        step += 1


def main():
    default_grammar = """
    S -> C C
    C -> c C | d
    """

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    else:
        text = default_grammar

    load_grammar(text)
    build_clr1_states()
    build_clr1_table()
    print_table()

    # Input string
    test_tokens = ["c", "c", "d", "d"]
    if len(sys.argv) > 2:
        test_tokens = sys.argv[2].split()

    parse_string(test_tokens)


if __name__ == "__main__":
    main()
