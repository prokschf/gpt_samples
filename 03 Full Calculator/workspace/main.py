from calculator import Calculator

def main():
    input_string = input("Enter a mathematical expression: ")
    calculator = Calculator(input_string)
    try:
        result = calculator.calculate()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
