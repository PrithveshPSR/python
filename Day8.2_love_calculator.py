def calculate_love_score1(name1, name2):
    # Combine the names and convert them to lowercase
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    # Count occurrences of the letters in "TRUE"
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    # Count occurrences of the letters in "LOVE"
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")  # This is fine, as we are recalculating it
    second_digit = l + o + v + e
    
    # Combine the two counts to form a love score
    score = int(str(first_digit) + str(second_digit))
    print(f"Love Score (Method 1): {score}")

def calculate_love_score_normalized(name1, name2):
    # Convert both names to lowercase to make the search case insensitive
    combined_names = (name1 + name2).lower()
    
    # Define the characters we are interested in for "TRUE" and "LOVE"
    true_letters = "true"
    love_letters = "love"
    
    # Calculate the number of occurrences for TRUE letters
    true_count = sum(combined_names.count(char) for char in true_letters)
    
    # Calculate the number of occurrences for LOVE letters
    love_count = sum(combined_names.count(char) for char in love_letters)
    
    # Combine the counts to form a two-digit number
    love_score = int(str(true_count) + str(love_count))
    
    # Normalize the score to out of 100 for better understanding
    max_score = 99  # max score based on the max combination of true_count and love_count
    love_percentage = (love_score / max_score) * 100
    
    # Print the love score and percentage
    print(f"Love Score (Method 2): {love_score}")
    print(f"Love Percentage: {love_percentage:.2f}%")

def main():
    while True:
        # Ask the user for the names
        name1 = input("Enter the first name: ")
        name2 = input("Enter the second name: ")
        
        # Calculate and display the love score using both methods
        calculate_love_score1(name1, name2)
        calculate_love_score_normalized(name1, name2)
        
        # Ask if the user wants to continue
        continue_choice = input("Do you want to continue? (y/n): ").lower()
        if continue_choice != 'y':
            print("Goodbye!")
            break

# Run the main function to start the program
if __name__ == "__main__":
    main()
