import sys
from calculator import Calculator

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py number1 operation number2")
        return

    num1, operation, num2 = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Both numbers must be valid numbers")
        return

    calculator = Calculator()

    if operation == "+":
        result = calculator.add(num1, num2)
    elif operation == "-":
        result = calculator.subtract(num1, num2)
    elif operation == "*":
        result = calculator.multiply(num1, num2)
    elif operation == "/":
        try:
            result = calculator.divide(num1, num2)
        except ValueError as e:
            print(str(e))
            return
    elif operation == "^":
        try:
            result = calculator.power(num1, num2)
        except ValueError as e:
            print(str(e))
            return
    else:
        print("Invalid operation. Must be one of +, -, *, /, ^")
        return

    print(result)

if __name__ == "__main__":
    main()
