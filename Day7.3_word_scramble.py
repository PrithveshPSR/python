import random

def word_scramble_game():
    # List of words to choose from
    words = ["developer", "persistence", "equifax", "transamerica", "kafka", "scala"]
    
    # Select a random word
    word = random.choice(words).lower()
    scrambled_word = "".join(random.sample(word, len(word)))  # Scramble the letters of the word
    attempts = 3  # Number of attempts to guess the word
    
    print("Welcome to the Word Scramble Game!")
    print(f"Here is your scrambled word: {scrambled_word}")
    print(f"You have {attempts} attempts to guess the original word. Good luck!")
    
    while attempts > 0:
        guess = input("\nGuess the word: ").lower()
        
        if guess == word:
            print("\nCongratulations! You've guessed the word correctly!")
            break
        else:
            attempts -= 1
            print(f"Incorrect guess! Attempts remaining: {attempts}")
    
    if attempts == 0:
        print(f"\nGame Over! The correct word was: '{word}'")

# Run the Word Scramble game
if __name__ == "__main__":
    word_scramble_game()
