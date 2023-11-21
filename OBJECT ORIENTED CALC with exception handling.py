class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2

    def subtract(self, num1, num2):
        self.result = num1 - num2

    def multiply(self, num1, num2):
        self.result = num1 * num2

    def divide(self, num1, num2):
        try:
            result = num1/num2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print("Result: {result}")

    def get_result(self):
        return self.result

calculator = Calculator()

while True:

    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        if user_input == "add":
            calculator.add(num1, num2)
        elif user_input == "subtract":
            calculator.subtract(num1, num2)
        elif user_input == "multiply":
            calculator.multiply(num1, num2)
        elif user_input == "divide":
            calculator.divide(num1, num2)
        print("Result:", calculator.get_result())
    else:
        print("Invalid input. Please try again.")
