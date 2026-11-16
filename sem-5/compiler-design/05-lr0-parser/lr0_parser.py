# ==============================================================================
# Practical 05: LR(0) Parser
# Simple Canonical LR(0) item generation, parsing table construction, and parsing
# ==============================================================================

import sys

productions = []  # list of tuples: (head, [symbols])
non_terminals = []
terminals = []
start_symbol = None

states = []  # list of sets of items: (prod_idx, dot_pos)
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

    # Add augmented production: S' -> S
    aug_start = start_symbol + "'"
    productions.insert(0, (aug_start, [start_symbol]))
    non_terminals.insert(0, aug_start)

    # Collect terminals
    terms = set()
    for head, body in productions:
        for s in body:
            if s not in non_terminals:
                terms.add(s)
    terminals = sorted(list(terms))


def closure(items):
    """Find closure of a set of items (prod_idx, dot_pos)."""
    current_set = set(items)
    changed = True
    while changed:
        changed = False
        new_items = set()
        for prod_idx, dot in current_set:
            head, body = productions[prod_idx]
            # Check if dot is before a non-terminal B
            if dot < len(body):
                symbol_after_dot = body[dot]
                if symbol_after_dot in non_terminals:
                    # Add all productions of B with dot at position 0
                    for p_idx, (p_head, p_body) in enumerate(productions):
                        if p_head == symbol_after_dot:
                            item = (p_idx, 0)
                            if item not in current_set and item not in new_items:
                                new_items.add(item)
                                changed = True
        current_set.update(new_items)
    return current_set


def goto(items, symbol):
    """Move the dot across 'symbol' and compute closure."""
    moved = set()
    for prod_idx, dot in items:
        head, body = productions[prod_idx]
        if dot < len(body) and body[dot] == symbol:
            moved.add((prod_idx, dot + 1))
    return closure(moved) if moved else set()


def build_states():
    global states, transitions
    # Initial state I0
    i0 = closure([(0, 0)])
    states = [i0]
    transitions = {}

    all_symbols = non_terminals + terminals
    queue = [0]

    while queue:
        curr_idx = queue.pop(0)
        curr_state = states[curr_idx]

        for sym in all_symbols:
            next_state = goto(curr_state, sym)
            if not next_state:
                continue

            # Check if this state already exists
            if next_state not in states:
                states.append(next_state)
                new_idx = len(states) - 1
                queue.append(new_idx)
            else:
                new_idx = states.index(next_state)

            transitions[(curr_idx, sym)] = new_idx


def build_lr0_table():
    global action_table, goto_table
    action_cols = terminals + ["$"]
    goto_cols = [nt for nt in non_terminals if nt != productions[0][0]]

    action_table = {i: {t: None for t in action_cols} for i in range(len(states))}
    goto_table = {i: {nt: None for nt in goto_cols} for i in range(len(states))}

    for i, state in enumerate(states):
        for prod_idx, dot in state:
            head, body = productions[prod_idx]

            # Shift condition: dot is before a terminal
            if dot < len(body):
                sym = body[dot]
                if sym in terminals and (i, sym) in transitions:
                    next_st = transitions[(i, sym)]
                    action_table[i][sym] = f"s{next_st}"
            else:
                # Reduce condition: dot is at the end
                if prod_idx == 0:
                    action_table[i]["$"] = "acc"
                else:
                    # In LR(0), reduce action is placed in ALL terminal columns + $
                    for t in action_cols:
                        action_table[i][t] = f"r{prod_idx}"

        # Goto transitions for non-terminals
        for nt in goto_cols:
            if (i, nt) in transitions:
                goto_table[i][nt] = transitions[(i, nt)]


def print_table():
    print("-" * 65)
    print("                     LR(0) PARSING TABLE")
    print("-" * 65)
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

    print("\n" + "=" * 65)
    print(f"Parsing Input: {' '.join(tokens)}")
    print("=" * 65)
    print(f"{'Step':<6}{'State Stack':<18}{'Symbol Stack':<16}{'Input':<14}{'Action'}")
    print("-" * 65)

    while True:
        s = state_stack[-1]
        a = buffer[0]
        act = action_table[s].get(a)

        s_str = " ".join(str(x) for x in state_stack)
        sym_str = " ".join(symbol_stack)
        buf_str = " ".join(buffer)

        if act == "acc":
            print(f"{step:<6}{s_str:<18}{sym_str:<16}{buf_str:<14}ACCEPT (Parsed Successfully)")
            return True
        elif act and act.startswith("s"):
            # Shift
            next_s = int(act[1:])
            print(f"{step:<6}{s_str:<18}{sym_str:<16}{buf_str:<14}Shift state {next_s}")
            symbol_stack.append(a)
            state_stack.append(next_s)
            buffer.pop(0)
        elif act and act.startswith("r"):
            # Reduce
            p_idx = int(act[1:])
            head, body = productions[p_idx]
            print(f"{step:<6}{s_str:<18}{sym_str:<16}{buf_str:<14}Reduce by {head} -> {' '.join(body)}")
            # Pop length of RHS from both stacks
            for _ in range(len(body)):
                state_stack.pop()
                symbol_stack.pop()
            # Goto on new top of state stack
            top_state = state_stack[-1]
            goto_s = goto_table[top_state][head]
            symbol_stack.append(head)
            state_stack.append(goto_s)
        else:
            print(f"{step:<6}{s_str:<18}{sym_str:<16}{buf_str:<14}ERROR: Invalid transition")
            return False

        step += 1


def main():
    default_grammar = """
    S -> ( S )
    S -> a
    """

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    else:
        text = default_grammar

    load_grammar(text)
    build_states()
    build_lr0_table()
    print_table()

    # Test string
    test_tokens = ["(", "(", "a", ")", ")"]
    if len(sys.argv) > 2:
        test_tokens = sys.argv[2].split()

    parse_string(test_tokens)


if __name__ == "__main__":
    main()
