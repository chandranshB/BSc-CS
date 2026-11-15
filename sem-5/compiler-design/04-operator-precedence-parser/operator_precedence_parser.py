# ==============================================================================
# Practical 04: Operator Precedence Parser
# Simple shift-reduce parser using an operator precedence relation table
# ==============================================================================

import sys

# Terminals used in arithmetic expressions
TERMINALS = ["+", "*", "(", ")", "id", "$"]

# Precedence relations:
#   '<' means shift (yields precedence)
#   '>' means reduce (takes precedence)
#   '=' means equal precedence
#   ' ' means syntax error
PRECEDENCE_TABLE = {
    "+":  {"+": ">", "*": "<", "(": "<", ")": ">", "id": "<", "$": ">"},
    "*":  {"+": ">", "*": ">", "(": "<", ")": ">", "id": "<", "$": ">"},
    "(":  {"+": "<", "*": "<", "(": "<", ")": "=", "id": "<", "$": " "},
    ")":  {"+": ">", "*": ">", "(": " ", ")": ">", "id": " ", "$": ">"},
    "id": {"+": ">", "*": ">", "(": " ", ")": ">", "id": " ", "$": ">"},
    "$":  {"+": "<", "*": "<", "(": "<", ")": " ", "id": "<", "$": "ACCEPT"}
}


def print_table():
    print("-" * 55)
    print("          OPERATOR PRECEDENCE RELATION TABLE")
    print("-" * 55)
    header = f"{'Op':<6}" + "".join(f"{t:<8}" for t in TERMINALS)
    print(header)
    print("-" * len(header))
    for row_op in TERMINALS:
        line = f"{row_op:<6}"
        for col_op in TERMINALS:
            rel = PRECEDENCE_TABLE[row_op].get(col_op, " ")
            line += f"{rel:<8}"
        print(line)
    print("-" * len(header))
    print("Notation: '<' = Shift, '>' = Reduce, '=' = Equal\n")


def parse_expression(tokens):
    buffer = list(tokens) + ["$"]
    stack = ["$"]
    step = 1

    print("=" * 65)
    print(f"Parsing Expression: {' '.join(tokens)}")
    print("=" * 65)
    print(f"{'Step':<6}{'Stack':<20}{'Relation':<10}{'Input Buffer':<16}{'Action'}")
    print("-" * 65)

    while True:
        # Find the topmost terminal in the stack (ignore non-terminal 'E')
        top_idx = len(stack) - 1
        while top_idx >= 0 and stack[top_idx] not in TERMINALS:
            top_idx -= 1
        top_term = stack[top_idx]

        curr_token = buffer[0]
        rel = PRECEDENCE_TABLE[top_term].get(curr_token, " ")

        stack_str = " ".join(stack)
        buf_str = " ".join(buffer)

        # Check accept condition
        if top_term == "$" and curr_token == "$":
            print(f"{step:<6}{stack_str:<20}{' ':10}{buf_str:<16}ACCEPT (Parsed Successfully)")
            return True

        if rel == "<" or rel == "=":
            # Shift action
            print(f"{step:<6}{stack_str:<20}{rel:<10}{buf_str:<16}Shift '{curr_token}'")
            stack.append(curr_token)
            buffer.pop(0)
        elif rel == ">":
            # Reduce action
            if stack[-1] == "id":
                stack.pop()
                print(f"{step:<6}{stack_str:<20}{rel:<10}{buf_str:<16}Reduce 'id' -> E")
                stack.append("E")
            elif len(stack) >= 3 and stack[-3] == "E" and stack[-2] in ("+", "*") and stack[-1] == "E":
                op = stack[-2]
                stack.pop()
                stack.pop()
                stack.pop()
                print(f"{step:<6}{stack_str:<20}{rel:<10}{buf_str:<16}Reduce 'E {op} E' -> E")
                stack.append("E")
            elif len(stack) >= 3 and stack[-3] == "(" and stack[-2] == "E" and stack[-1] == ")":
                stack.pop()
                stack.pop()
                stack.pop()
                print(f"{step:<6}{stack_str:<20}{rel:<10}{buf_str:<16}Reduce '( E )' -> E")
                stack.append("E")
            else:
                popped = stack.pop()
                print(f"{step:<6}{stack_str:<20}{rel:<10}{buf_str:<16}Reduce '{popped}' -> E")
                stack.append("E")
        else:
            print(f"{step:<6}{stack_str:<20}{'ERROR':<10}{buf_str:<16}ERROR: Invalid relation between '{top_term}' and '{curr_token}'")
            return False

        step += 1


def main():
    print_table()

    # Default expression to parse
    tokens = ["id", "+", "id", "*", "id"]
    if len(sys.argv) > 1:
        tokens = sys.argv[1].split()

    parse_expression(tokens)


if __name__ == "__main__":
    main()
