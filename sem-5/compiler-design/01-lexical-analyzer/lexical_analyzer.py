# ==============================================================================
# Practical 01: Lexical Analyzer
# Simple scanner to identify keywords, identifiers, constants, operators & delimiters
# ==============================================================================

import sys

# Predefined sets of C tokens
KEYWORDS = ["int", "float", "char", "double", "if", "else", "while", "for", "return", "void"]
OPERATORS = ["==", "!=", "<=", ">=", "+=", "-=", "*=", "/=", "+", "-", "*", "/", "%", "=", "<", ">", "!", "&", "|"]
DELIMITERS = [";", ",", "(", ")", "{", "}", "[", "]"]


def remove_comments(code):
    """Simple function to remove single-line // and multi-line /* */ comments."""
    cleaned = []
    i = 0
    n = len(code)
    while i < n:
        # Check single line comment
        if i + 1 < n and code[i] == '/' and code[i + 1] == '/':
            while i < n and code[i] != '\n':
                i += 1
        # Check multi line comment
        elif i + 1 < n and code[i] == '/' and code[i + 1] == '*':
            i += 2
            while i + 1 < n and not (code[i] == '*' and code[i + 1] == '/'):
                i += 1
            i += 2
        else:
            cleaned.append(code[i])
            i += 1
    return "".join(cleaned)


def is_number(s):
    """Check if string is an integer or float."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def tokenize(source_code):
    clean_code = remove_comments(source_code)
    tokens = []
    symbol_table = []

    lines = clean_code.split('\n')
    for line_no, line in enumerate(lines, start=1):
        i = 0
        n = len(line)
        while i < n:
            ch = line[i]

            # 1. Skip spaces and tabs
            if ch.isspace():
                i += 1
                continue

            # 2. String literal: "hello"
            if ch == '"':
                start = i
                i += 1
                while i < n and line[i] != '"':
                    i += 1
                i += 1  # closing quote
                token_val = line[start:i]
                tokens.append((line_no, "STRING_LITERAL", token_val))
                continue

            # 3. Character literal: 'a'
            if ch == "'":
                start = i
                i += 1
                while i < n and line[i] != "'":
                    i += 1
                i += 1
                token_val = line[start:i]
                tokens.append((line_no, "CHAR_LITERAL", token_val))
                continue

            # 4. Check two-character operators first (e.g., ==, <=, +=)
            two_char = line[i:i+2]
            if two_char in OPERATORS:
                tokens.append((line_no, "OPERATOR", two_char))
                i += 2
                continue

            # 5. Check single-character operator
            if ch in OPERATORS:
                tokens.append((line_no, "OPERATOR", ch))
                i += 1
                continue

            # 6. Check delimiter
            if ch in DELIMITERS:
                tokens.append((line_no, "DELIMITER", ch))
                i += 1
                continue

            # 7. Number constant (integer or float)
            if ch.isdigit():
                start = i
                while i < n and (line[i].isdigit() or line[i] == '.'):
                    i += 1
                num_val = line[start:i]
                tokens.append((line_no, "CONSTANT", num_val))
                continue

            # 8. Identifier or Keyword
            if ch.isalpha() or ch == '_':
                start = i
                while i < n and (line[i].isalnum() or line[i] == '_'):
                    i += 1
                word = line[start:i]
                if word in KEYWORDS:
                    tokens.append((line_no, "KEYWORD", word))
                else:
                    tokens.append((line_no, "IDENTIFIER", word))
                    # Add to symbol table if not already added
                    if word not in symbol_table:
                        symbol_table.append(word)
                continue

            # Unrecognized symbol
            tokens.append((line_no, "UNKNOWN", ch))
            i += 1

    return tokens, symbol_table


def main():
    # If a file is given as argument, read it. Otherwise use sample code.
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            code = f.read()
    else:
        code = """
        int main() {
            int num = 5;
            float fact = 1.0;
            char grade = 'A';
            // calculate factorial
            while (num > 0) {
                fact = fact * num;
                num = num - 1;
            }
            return 0;
        }
        """

    tokens, symbol_table = tokenize(code)

    print("-" * 50)
    print("                LEXICAL TOKENS")
    print("-" * 50)
    print(f"{'Line':<8}{'Token Type':<18}{'Lexeme'}")
    print("-" * 50)
    for line_no, token_type, lexeme in tokens:
        print(f"{line_no:<8}{token_type:<18}{lexeme}")

    print("\n" + "-" * 50)
    print("                 SYMBOL TABLE")
    print("-" * 50)
    print(f"{'S.No':<8}{'Identifier'}")
    print("-" * 50)
    for idx, name in enumerate(symbol_table, start=1):
        print(f"{idx:<8}{name}")
    print("-" * 50)


if __name__ == "__main__":
    main()
