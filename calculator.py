# Simple Interactive Calculator
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Oops! You can't divide by zero."
    else:
        return "that doesn't look like a valid operation."

print("Welcome to the Simple Calculator!")
print("You can add (+), subtract (-), multiply (*), or divide (/).")

#input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ").strip()

    #calculation
    result = calculate(num1, num2, operation)

    #result
    print(f"\nYour result: {num1} {operation} {num2} = {result}")
    print("Thanks for using the calculator! 🎉")
except ValueError:
    print("That doesn't seem like a valid number. Please try again.")
