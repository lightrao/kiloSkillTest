"""
This module provides basic calculator functionality including addition,
subtraction, multiplication, and division.
"""

def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts the second number from the first and returns the result."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

def divide(x, y):
    """Divides the first number by the second and returns the result.
    Handles division by zero error.
    """
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    """Main function to handle user input and perform calculations."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                # Perform addition
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                # Perform subtraction
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                # Perform multiplication
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                # Perform division
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            
            # Ask if user wants another calculation
            next_calculation = input("Let's do another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
