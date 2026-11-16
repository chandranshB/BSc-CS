# ==============================================================================
# Practical 06: SLR(1) Parser (Simple LR)
# Uses LR(0) items + FOLLOW sets to resolve reduce actions without conflicts
# ==============================================================================

import sys

productions = []  # (head, [symbols])
non_terminals = []
terminals = []
start_symbol = None

states = []
transitions = {}
follow = {}
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

    # Add augmented production S' -> S
    aug_start = start_symbol + "'"
    productions.insert(0, (aug_start, [start_symbol]))
    non_terminals.insert(0, aug_start)

    terms = set()
    for head, body in productions:
        for s in body:
            if s not in non_terminals:
                terms.add(s)
    terminals = sorted(list(terms))


def find_first(symbol):
    if symbol in terminals or symbol == "#":
        return {symbol}
    res = set()
    for head, body in productions:
        if head == symbol:
            for s in body:
                sf = find_first(s)
                res.update(sf - {"#"})
                if "#" not in sf:
                    break
            else:
                res.add("#")
    return res


def compute_follow():
    global follow
    follow = {nt: set() for nt in non_terminals}
    # Put $ in FOLLOW of augmented start and original start
    follow[productions[0][0]].add("$")
    follow[start_symbol].add("$")

    changed = True
    while changed:
        changed = False
        for head, body in productions:
            for i in range(len(body)):
                curr = body[i]
                if curr in non_terminals:
                    before = len(follow[curr])
                    rest = body[i + 1:]
                    if rest:
                        rest_first = set()
                        for s in rest:
                            sf = find_first(s)
                            rest_first.update(sf - {"#"})
                            if "#" not in sf:
                                break
                        else:
                            rest_first.update(follow[head])
                        follow[curr].update(rest_first)
                    else:
                        follow[curr].update(follow[head])

                    if len(follow[curr]) > before:
                        changed = True


def closure(items):
    current_set = set(items)
    changed = True
    while changed:
        changed = False
        new_items = set()
        for prod_idx, dot in current_set:
            head, body = productions[prod_idx]
            if dot < len(body):
                sym_after_dot = body[dot]
                if sym_after_dot in non_terminals:
                    for p_idx, (p_head, p_body) in enumerate(productions):
                        if p_head == sym_after_dot:
                            item = (p_idx, 0)
                            if item not in current_set and item not in new_items:
                                new_items.add(item)
                                changed = True
        current_set.update(new_items)
    return current_set


def goto(items, symbol):
    moved = set()
    for prod_idx, dot in items:
        head, body = productions[prod_idx]
        if dot < len(body) and body[dot] == symbol:
            moved.add((prod_idx, dot + 1))
    return closure(moved) if moved else set()


def build_states():
    global states, transitions
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

            if next_state not in states:
                states.append(next_state)
                new_idx = len(states) - 1
                queue.append(new_idx)
            else:
                new_idx = states.index(next_state)

            transitions[(curr_idx, sym)] = new_idx


def build_slr1_table():
    global action_table, goto_table
    action_cols = terminals + ["$"]
    goto_cols = [nt for nt in non_terminals if nt != productions[0][0]]

    action_table = {i: {t: None for t in action_cols} for i in range(len(states))}
    goto_table = {i: {nt: None for nt in goto_cols} for i in range(len(states))}

    for i, state in enumerate(states):
        for prod_idx, dot in state:
            head, body = productions[prod_idx]

            # Shift condition
            if dot < len(body):
                sym = body[dot]
                if sym in terminals and (i, sym) in transitions:
                    next_s = transitions[(i, sym)]
                    action_table[i][sym] = f"s{next_s}"
            else:
                # Reduce condition: Only place reduce for terminals in FOLLOW(head)
                if prod_idx == 0:
                    action_table[i]["$"] = "acc"
                else:
                    for t in follow[head]:
                        action_table[i][t] = f"r{prod_idx}"

        # GOTO table
        for nt in goto_cols:
            if (i, nt) in transitions:
                goto_table[i][nt] = transitions[(i, nt)]


def print_table():
    print("-" * 75)
    print("                         SLR(1) PARSING TABLE")
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
            top_state = state_stack[-1]
            goto_s = goto_table[top_state][head]
            symbol_stack.append(head)
            state_stack.append(goto_s)
        else:
            print(f"{step:<6}{s_str:<22}{sym_str:<18}{buf_str:<16}ERROR: Syntax Error at state {s} with '{a}'")
            return False

        step += 1


def main():
    default_grammar = """
    E -> E + T | T
    T -> T * F | F
    F -> ( E ) | id
    """

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    else:
        text = default_grammar

    load_grammar(text)
    compute_follow()
    build_states()
    build_slr1_table()
    print_table()

    # Input expression
    test_tokens = ["id", "+", "id", "*", "id"]
    if len(sys.argv) > 2:
        test_tokens = sys.argv[2].split()

    parse_string(test_tokens)


if __name__ == "__main__":
    main()
