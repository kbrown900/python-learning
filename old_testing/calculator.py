# Define functions for each arithmetic operation
def add(x, y):
    """Function to perform addition"""
    return x + y

def subtract(x, y):
    """Function to perform subtraction"""
    return x - y

def multiply(x, y):
    """Function to perform multiplication"""
    return x * y

def divide(x, y):
    """Function to perform division, checks for division by zero"""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Map operations to their corresponding functions using a dictionary
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Get user input for the first number, operation, and second number
first_number = float(input("Enter the first number: "))
operation = input("Enter operation (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

# Check if the chosen operation is valid
if operation in operations:
    # Retrieve the function corresponding to the chosen operation
    result = operations[operation](first_number, second_number)
    print(f"Result: {result}")
else:
    # Handle invalid operations
    print("Error: Invalid operation.")