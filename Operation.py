# Function to perform arithmetic operations
def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

# Take input from the user
print("Welcome to the Arithmetic Operations Program")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

# Perform the operation and display the result
result = arithmetic_operation(num1, num2, op)
print(f"The result of {num1} {op} {num2} is: {result}")
