import random

def hangman():
    # List of words for the game
    word_list = ["python", "developer", "hangman", "programming", "openai"]
    # Randomly select a word
    word = random.choice(word_list)
    guessed_word = ["_"] * len(word)  # Initialize blanks
    lives = 6  # Number of allowed incorrect guesses
    guessed_letters = set()  # Keep track of guessed letters

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))
    print(f"You have {lives} lives.")

    while lives > 0:
        guess = input("\nGuess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("Good guess!")
            # Replace blanks with the guessed letter
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            lives -= 1
            print(f"Wrong guess! You lose a life. Lives remaining: {lives}")

        print(" ".join(guessed_word))

        # Check if the player has guessed all letters
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

# Run the game
hangman()
