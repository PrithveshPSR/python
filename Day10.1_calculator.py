# Simple Python Calculator Program with Validation, Continuation Option, and Logo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def display_logo():
    logo = '''
      _____________________
     |  _________________  |
     | |              0. | |
     | |_________________| |
     |  ___ ___   ___    | |
     | | 7 | 8 | 9 | + |  | |
     | |___|___|___|___|  | |
     | | 4 | 5 | 6 | - |  | |
     | |___|___|___|___|  | |
     | | 1 | 2 | 3 | x |  | |
     | |___|___|___|___|  | |
     | | 0 | . | = | / |  | |
     | |___|___|___|___|  | |
     |_____________________| 
    '''
    print(logo)

def get_valid_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_valid_choice():
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            return choice
        else:
            print("Invalid choice! Please select a valid operation (1, 2, 3, or 4).")

def calculator():
    display_logo()  # Display the logo first

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = get_valid_choice()  # Get a valid operation choice

        num1 = get_valid_number("Enter first number: ")  # Get valid number input
        num2 = get_valid_number("Enter second number: ")  # Get valid number input
        
        # Perform the chosen operation
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        # Ask if the user wants to continue
        next_calculation = input("Do you want another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()