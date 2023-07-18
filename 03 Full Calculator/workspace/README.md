The core classes, functions, and methods necessary for this project are:

1. `Calculator`: This class will be responsible for parsing the input string and performing the calculations. It will have the following methods:
    - `__init__`: Initializes the Calculator with an input string.
    - `calculate`: Parses the input string and performs the calculations.
    - `next_token`: Helper method to get the next token from the input string.
    - `parse_expression`: Helper method to parse an expression from the input string.
    - `parse_term`: Helper method to parse a term from the input string.
    - `parse_factor`: Helper method to parse a factor from the input string.
    - `parse_number`: Helper method to parse a number from the input string.
    - `parse_parentheses`: Helper method to parse parentheses from the input string.
    - `error`: Helper method to throw an error.

2. `main`: This function will be the entry point of the program. It will create a Calculator instance and call its `calculate` method.

Now, let's write the code for each file.

calculator.py
