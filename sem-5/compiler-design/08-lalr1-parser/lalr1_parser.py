# ==============================================================================
# Practical 08: LALR(1) Parser (Look-Ahead LR)
# Merges CLR(1) states with identical LR(0) cores to produce a compact table
# ==============================================================================

import sys

productions = []  # (head, [symbols])
non_terminals = []
terminals = []
start_symbol = None

clr_states = []
clr_transitions = {}

lalr_states = []
lalr_state_names = {}
clr_to_lalr = {}
lalr_transitions = {}
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
    res = set()
    for s in seq:
        if s in terminals or s == "$":
            res.add(s)
            break
        elif s in non_terminals:
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
    global clr_states, clr_transitions
    i0 = lr1_closure([(0, 0, "$")])
    clr_states = [i0]
    clr_transitions = {}

    all_symbols = non_terminals + terminals
    queue = [0]

    while queue:
        curr_idx = queue.pop(0)
        curr_state = clr_states[curr_idx]

        for sym in all_symbols:
            next_st = lr1_goto(curr_state, sym)
            if not next_st:
                continue

            if next_st not in clr_states:
                clr_states.append(next_st)
                new_idx = len(clr_states) - 1
                queue.append(new_idx)
            else:
                new_idx = clr_states.index(next_st)

            clr_transitions[(curr_idx, sym)] = new_idx


def get_core(state):
    """The LR(0) core is the set of items without lookaheads: (prod_idx, dot)."""
    return frozenset((p_idx, dot) for p_idx, dot, la in state)


def merge_cores():
    """Group CLR(1) states that have the same core and merge their lookaheads."""
    global lalr_states, lalr_state_names, clr_to_lalr
    core_map = {}
    for idx, state in enumerate(clr_states):
        core = get_core(state)
        if core not in core_map:
            core_map[core] = []
        core_map[core].append(idx)

    lalr_states = []
    lalr_state_names = {}
    clr_to_lalr = {}

    for new_idx, (core, clr_indices) in enumerate(core_map.items()):
        # Combine items from all merged states
        merged_items = set()
        for c_idx in clr_indices:
            merged_items.update(clr_states[c_idx])

        lalr_states.append(merged_items)
        name = "I" + "_".join(str(x) for x in clr_indices)
        lalr_state_names[new_idx] = name

        for c_idx in clr_indices:
            clr_to_lalr[c_idx] = new_idx


def build_lalr_table():
    global lalr_transitions, action_table, goto_table
    lalr_transitions = {}

    # Map CLR transitions to LALR transitions
    for (from_c, sym), to_c in clr_transitions.items():
        lalr_from = clr_to_lalr[from_c]
        lalr_to = clr_to_lalr[to_c]
        lalr_transitions[(lalr_from, sym)] = lalr_to

    action_cols = terminals + ["$"]
    goto_cols = [nt for nt in non_terminals if nt != productions[0][0]]

    action_table = {i: {t: None for t in action_cols} for i in range(len(lalr_states))}
    goto_table = {i: {nt: None for nt in goto_cols} for i in range(len(lalr_states))}

    for i, state in enumerate(lalr_states):
        for prod_idx, dot, la in state:
            head, body = productions[prod_idx]

            # Shift
            if dot < len(body):
                sym = body[dot]
                if sym in terminals and (i, sym) in lalr_transitions:
                    next_s = lalr_transitions[(i, sym)]
                    action_table[i][sym] = f"s{next_s}"
            else:
                # Reduce under lookahead
                if prod_idx == 0 and la == "$":
                    action_table[i]["$"] = "acc"
                else:
                    action_table[i][la] = f"r{prod_idx}"

        for nt in goto_cols:
            if (i, nt) in lalr_transitions:
                goto_table[i][nt] = lalr_transitions[(i, nt)]


def print_table():
    print("-" * 65)
    print(f"LALR(1) Merged States: {len(clr_states)} CLR states -> {len(lalr_states)} LALR states")
    for idx, name in lalr_state_names.items():
        print(f"  State {idx}: {name}")
    print("-" * 65)

    print("\n" + "-" * 75)
    print("                         LALR(1) PARSING TABLE")
    print("-" * 75)
    action_cols = terminals + ["$"]
    goto_cols = [nt for nt in non_terminals if nt != productions[0][0]]

    header = f"{'State':<10}| " + "".join(f"{a:<7}" for a in action_cols) + "| " + "".join(f"{g:<7}" for g in goto_cols)
    print(header)
    print("-" * len(header))
    for i in range(len(lalr_states)):
        st_lbl = f"{i} ({lalr_state_names[i]})"
        row = f"{st_lbl:<10}| "
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
    merge_cores()
    build_lalr_table()
    print_table()

    # Input string
    test_tokens = ["c", "c", "d", "d"]
    if len(sys.argv) > 2:
        test_tokens = sys.argv[2].split()

    parse_string(test_tokens)


if __name__ == "__main__":
    main()
