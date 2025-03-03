# Define functions for basic arithmetic operations
def add(x, y):
    """This function adds two numbers and returns the result."""
    return x + y
def subtract(x, y):
    """This function subtracts the second number from the first and returns the result."""
    return x - y
def multiply(x, y):
    """This function multiplies two numbers and returns the result."""
    return x * y
def divide(x, y):
    """This function divides the first number by the second and returns the result.
    It includes a check to prevent division by zero."""
    if y == 0:
        return "Error! Division by zero."
    return x / y
# Display the menu for the user to choose an operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
# Take user input for the operation choice
choice = input("Enter choice(1/2/3/4): ")
# Take user input for the numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Perform the chosen operation and display the result
if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input")
