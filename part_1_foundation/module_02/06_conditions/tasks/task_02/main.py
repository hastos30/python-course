number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
op = input("Enter operation + - * / // %: ").strip()

if op not in ("+", "-", "*", "/", "//", "%"):
    print("Invalid operation")
elif op == "+":
    print(f"Result: {number1 + number2:.2f}")
elif op == "-":
    print(f"Result: {number1 - number2:.2f}")
elif op == "*":
    print(f"Result: {number1 * number2:.2f}")
elif op in ("/", "//", "%"):
    if number2 == 0:
        print("Error: division by zero")
    else:
        if op == "/":
            print(f"Result: {number1 / number2:.2f}")
        elif op == "//":
            print(f"Result: {number1 // number2:.2f}")
        else:
            print(f"Result: {number1 % number2:.2f}")
