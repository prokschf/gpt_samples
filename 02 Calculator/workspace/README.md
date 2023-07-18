The architecture of the calculator tool will consist of two main parts:

1. A Calculator class that will perform the mathematical operations.
2. A main function that will handle the command line input and output.

The Calculator class will have the following methods:

- `add`: Adds two numbers.
- `subtract`: Subtracts the second number from the first.
- `multiply`: Multiplies two numbers.
- `divide`: Divides the first number by the second. Throws an error if the second number is zero.
- `power`: Raises the first number to the power of the second. Throws an error if the power is not an integer.

The main function will:

- Parse the command line input.
- Create an instance of the Calculator class.
- Call the appropriate method of the Calculator class based on the operation specified in the command line input.
- Print the result of the operation.
- Handle any errors that occur during the operation.

Now, let's write the code for each part of the architecture.

calculator.py
