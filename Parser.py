class TopDownParser:
    def _init_(self):
        self.grammar = {}
        self.start_symbol = None

    def add_rule(self, non_terminal, production):
        if non_terminal not in self.grammar:
            self.grammar[non_terminal] = []
        self.grammar[non_terminal].append(production)

    def set_start_symbol(self, symbol):
        self.start_symbol = symbol

    def parse(self, sequence):
        return self._parse_recursive(self.start_symbol, sequence)

    def _parse_recursive(self, current_symbol, sequence):
        if not sequence:
            return current_symbol == ''

        if current_symbol not in self.grammar:
            if sequence and current_symbol == sequence[0]:
                return self._parse_recursive('', sequence[1:])
            return False

        for production in self.grammar[current_symbol]:
            if self._parse_recursive(production, sequence):
                return True

        return False

    def is_simple_grammar(self):
        # Check if the grammar is simple (no left recursion and no epsilon productions)
        for non_terminal, productions in self.grammar.items():
            for production in productions:
                if production == '':
                    return False  # Epsilon production found
                if non_terminal in production:
                    return False  # Left recursion found
        return True


def main():
    parser = TopDownParser()

    print("Enter the start symbol:")
    start_symbol = input().strip()
    parser.set_start_symbol(start_symbol)

    print("Enter the grammar rules (format: A -> a | b | ...). Type 'done' when finished:")
    while True:
        rule = input().strip()
        if rule.lower() == 'done':
            break
        try:
            non_terminal, production = rule.split('->')
            non_terminal = non_terminal.strip()
            productions = production.split('|')
            for prod in productions:
                parser.add_rule(non_terminal, prod.strip())
        except ValueError:
            print("Invalid rule format. Please use 'A -> a | b | ...' format.")

    if not parser.is_simple_grammar():
        print("The grammar is not simple.")
        return

    while True:
        print("Enter a sequence to parse (or type 'exit' to quit):")
        sequence = input().strip()
        if sequence.lower() == 'exit':
            break
        if parser.parse(sequence):
            print("Accepted")
        else:
            print("Rejected")


if _name_ == "_main_":
    main()
