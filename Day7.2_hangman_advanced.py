import random

def display_hangman(lives):
    stages = [
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """
    ]
    return stages[lives]

def hangman_advanced():
    # Words, hints, and difficulty levels
    word_list = [
        {"word": "python", "hint": "A popular programming language", "difficulty": "easy"},
        {"word": "developer", "hint": "A person who writes software", "difficulty": "easy"},
        {"word": "polymorphism", "hint": "An OOP concept", "difficulty": "medium"},
        {"word": "asynchronous", "hint": "A programming technique for concurrency", "difficulty": "medium"},
        {"word": "cryptocurrency", "hint": "A decentralized digital currency", "difficulty": "hard"},
        {"word": "neuralnetwork", "hint": "A machine learning architecture", "difficulty": "hard"}
    ]

    print("\nWelcome to Advanced Hangman!")
    print("Select Difficulty Level:")
    print("1. Easy (6 lives)")
    print("2. Medium (4 lives)")
    print("3. Hard (3 lives)")

    while True:
        difficulty_choice = input("Enter your choice (1/2/3): ")
        if difficulty_choice in ["1", "2", "3"]:
            break
        print("Invalid choice. Please select 1, 2, or 3.")

    if difficulty_choice == "1":
        difficulty = "easy"
        lives = 6
    elif difficulty_choice == "2":
        difficulty = "medium"
        lives = 4
    else:
        difficulty = "hard"
        lives = 3

    score = 0  # Initialize score
    play_again = True

    while play_again:
        # Filter words by selected difficulty
        words_by_difficulty = [word for word in word_list if word["difficulty"] == difficulty]
        selected = random.choice(words_by_difficulty)
        word = selected["word"]
        hint = selected["hint"]

        guessed_word = ["_"] * len(word)  # Initialize blanks
        guessed_letters = set()  # Track guessed letters

        print("\nNew Round!")
        print(f"Hint: {hint}")
        print(" ".join(guessed_word))

        while lives > 0:
            print(display_hangman(lives))
            guess = input("\nGuess a letter: ").lower().strip()

            # Validate input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.add(guess)

            # Check if the guessed letter is in the word
            if guess in word:
                print("Great! You guessed a correct letter.")
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
            else:
                lives -= 1
                print(f"Oops! The letter '{guess}' is not in the word. Lives remaining: {lives}")

            print("\nCurrent word: " + " ".join(guessed_word))
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

            # Check if the player has guessed the word
            if "_" not in guessed_word:
                print("\n🎉 Congratulations! You guessed the word!")
                print(f"The word was: {word}")
                score += len(word) * lives  # Add to score based on word length and remaining lives
                print(f"Your current score: {score}")
                break
        else:
            print(display_hangman(lives))
            print("\n😢 Game Over! You've run out of lives.")
            print(f"The word was: {word}")
            print(f"Your final score: {score}")
            break

        # Ask if the player wants to play another round
        while True:
            play_again_choice = input("\nDo you want to play another round? (yes/no): ").lower().strip()
            if play_again_choice in ["yes", "no"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again_choice == "no":
            play_again = False
            print(f"Thank you for playing! Your final score: {score}")

# Run the advanced game
hangman_advanced()
