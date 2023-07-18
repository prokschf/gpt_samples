class Calculator:
    def __init__(self, input_string):
        self.input_string = input_string
        self.position = 0
        self.current_token = self.next_token()

    def error(self, message):
        raise Exception(message)

    def next_token(self):
        while self.position < len(self.input_string) and self.input_string[self.position].isspace():
            self.position += 1
        if self.position >= len(self.input_string):
            return None
        if zself.input_string[self.position].isdigit():
            start = self.position
            while self.position < len(self.input_string) and self.input_string[self.position].isdigit():
                self.position += 1
            return int(self.input_string[start:self.position])
        token = self.input_string[self.position]
        self.position += 1
        return token

    def parse_expression(self):
        term = self.parse_term()
        while self.current_token in ['+', '-']:
            if self.current_token == '+':
                self.current_token = self.next_token()
                term += self.parse_term()
            elif self.current_token == '-':
                self.current_token = self.next_token()
                term -= self.parse_term()
        return term

    def parse_term(self):
        factor = self.parse_factor()
        while self.current_token in ['*', '/']:
            if self.current_token == '*':
                self.current_token = self.next_token()
                factor *= self.parse_factor()
            elif self.current_token == '/':
                self.current_token = self.next_token()
                denominator = self.parse_factor()
                if denominator == 0:
                    self.error("Division by zero")
                factor /= denominator
        return factor

    def parse_factor(self):
        if self.current_token == '(':
            self.current_token = self.next_token()
            factor = self.parse_expression()
            if self.current_token != ')':
                self.error("Mismatched parentheses")
            self.current_token = self.next_token()
        elif self.current_token.isdigit():
            factor = self.parse_number()
        else:
            self.error("Invalid character")
        return factor

    def parse_number(self):
        number = self.current_token
        self.current_token = self.next_token()
        return number

    def calculate(self):
        result = self.parse_expression()
        if self.current_token is not None:
            self.error("Invalid expression")
        return result
