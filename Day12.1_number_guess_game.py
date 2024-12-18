import random

def display_logo():
    logo = """
    ##########################
    #  Number Guessing Game  #
    ##########################
    """
    print(logo)

def choose_level():
    print("Choose a difficulty level:")
    print("1. Easy (Range 1-50, 10 attempts)")
    print("2. Hard (Range 1-100, 5 attempts)")

    while True:
        level = input("Enter 1 for Easy or 2 for Hard: ")
        if level == "1":
            return "Easy", 1, 50, 10
        elif level == "2":
            return "Hard", 1, 100, 5
        else:
            print("Invalid input. Please enter 1 for Easy or 2 for Hard.")

def play_game():
    # Choose difficulty level
    level, low, high, max_attempts = choose_level()
    
    print(f"\nYou chose {level} mode.")
    print(f"I am thinking of a number between {low} and {high}. You have {max_attempts} attempts to guess it.")
    
    # Generate a random number based on difficulty level
    number_to_guess = random.randint(low, high)
    
    attempts = 0
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")
        
        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # Check if the guess is correct
        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            return attempts  # Return the number of attempts taken to guess the number
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
        return attempts  # Return the number of attempts used

def number_guessing_game():
    display_logo()

    total_score = 0  # Total score, lower score is better (fewer attempts)
    games_played = 0  # To track number of games played

    while True:
        print("\nStarting a new game...")
        attempts = play_game()
        games_played += 1
        total_score += attempts  # Add the number of attempts taken to the score

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another game? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

    # Final score after all games played
    print(f"\nGame Over! You played {games_played} games.")
    print(f"Your total attempts across all games: {total_score}")
    print(f"Your average score per game: {total_score / games_played:.2f} attempts")

# Run the game
number_guessing_game()
