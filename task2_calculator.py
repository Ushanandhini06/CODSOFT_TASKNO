print("===== SIMPLE CALCULATOR =====")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")
        result = None
else:
    print("Invalid operation.")
    result = None
if result is not None:
    print("Result =", result)