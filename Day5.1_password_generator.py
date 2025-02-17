import random
import string

def generate_password():
    # Ask for user input
    letters_count = int(input("How many letters would you like in your password? "))
    symbols_count = int(input("How many symbols would you like? "))
    numbers_count = int(input("How many numbers would you like? "))
    
    # Define the character sets
    letters = string.ascii_letters  # All uppercase and lowercase letters
    symbols = string.punctuation  # All symbols
    numbers = string.digits  # All numbers
    
    # Generate password components
    password_letters = random.choices(letters, k=letters_count)
    password_symbols = random.choices(symbols, k=symbols_count)
    password_numbers = random.choices(numbers, k=numbers_count)
    
    # Combine all parts
    password_list = password_letters + password_symbols + password_numbers
    
    # Shuffle the password list to make it random
    random.shuffle(password_list)
    
    # Join the list into a string
    password = ''.join(password_list)
    
    # Output the generated password
    print(f"Your password is: {password}")

# Run the function
generate_password()
