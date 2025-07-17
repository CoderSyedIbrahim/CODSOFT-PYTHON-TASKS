def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print("Result:", num1 + num2)
        elif operator == '-':
            print("Result:", num1 - num2)
        elif operator == '*':
            print("Result:", num1 * num2)
        elif operator == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operation.")
    except ValueError:
        print("Please enter valid numbers.")

calculator()