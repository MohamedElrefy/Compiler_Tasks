import re

# Define token types
token_specification = [
    ('COMMENT', r'//.*|/\*[\s\S]*?\*/'),  # Single-line and multi-line comments
    ('KEYWORD', r'\b(?:int|float|char|if|else|while|for|return|void|struct|typedef|const)\b'),  # C keywords
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),  # Identifiers
    ('NUMBER', r'\b\d+(\.\d+)?\b'),  # Integer or decimal numbers
    ('OPERATOR', r'[+\-*/%=!<>&|]'),  # Operators
    ('PUNCTUATION', r'[;,\(\){}]'),  # Punctuation characters
    ('STRING', r'"([^"\\]|\\.)*"'),  # String literals
    ('WHITESPACE', r'\s+'),  # Whitespace (ignored)
]

# Compile token regex patterns
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
token_compiler = re.compile(token_regex)


def scanner(code):
    tokens = []
    line_num = 1
    line_start = 0

    for match in token_compiler.finditer(code):
        kind = match.lastgroup
        value = match.group()
        column = match.start() - line_start

        if kind == 'WHITESPACE':
            if '\n' in value:
                line_num += value.count('\n')
                line_start = match.end()
            continue
        elif kind == 'COMMENT':
            continue

        tokens.append((kind, value, line_num, column))

    return tokens


def main():
    print("C Language Scanner")
    print("Choose an option:")
    print("1. Enter C code directly")
    print("2. Load C code from a file")

    option = input("Enter option (1 or 2): ")

    if option == '1':
        print("\nEnter your C code (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        code = "\n".join(lines)

    elif option == '2':
        file_path = input("Enter the file path: ")
        try:
            with open(file_path, 'r') as file:
                code = file.read()
        except FileNotFoundError:
            print("Error: File not found.")
            return

    else:
        print("Invalid option. Exiting.")
        return


    tokens = scanner(code)

    # Display tokens
    print("\nTokens found:")
    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
