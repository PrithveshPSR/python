import random

# ASCII art for Rock, Paper, and Scissors
ascii_art = {
    0: """
    _______
---'   ____
      (_____)
      (_____)
      (____)
---.__(___)
""",
    1: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    2: """
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

game_images = [0,1,2]

# Function to get user's choice
def get_user_choice():
    print("Enter your choice (0: Rock, 1: Paper, 2: Scissors):")
    try:
        user_choice = int(input())
        while user_choice not in [0, 1, 2]:
            print("Invalid choice! Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")
            user_choice = int(input())
            
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return get_user_choice()  # Recurse if input is invalid
    return user_choice

# Function to get computer's choice
def get_computer_choice():
    return random.randint(0, 2)  # Random choice between 0, 1, and 2
    

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    # Get choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    # Display the choices
    print(f"\nYour choice: {user_choice}{ascii_art[user_choice]}")
    print(f"Computer's choice: {computer_choice}{ascii_art[computer_choice]}")
    
    # Determine and display the result
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
if __name__ == "__main__":
    play_game()
