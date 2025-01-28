import random

# List of adjectives and nouns
adjectives = ['Electric', 'Fuzzy', 'Cosmic', 'Neon', 'Silent', 'Lunar', 'Golden', 'Phantom', 'Dark', 'Solar']
nouns = ['Waves', 'Vibe', 'Machine', 'Echo', 'Dream', 'Ghost', 'Panic', 'Storm', 'Beat', 'Galaxy']

# Function to generate a band name
def generate_band_name(user_name, city):
    adj = random.choice(adjectives)  # Pick a random adjective
    noun = random.choice(nouns)  # Pick a random noun
    band_name = f"{user_name}'s {adj} {noun} from {city}"  # Create band name with user's name and city
    return band_name

# Get user input for name and city during runtime
if __name__ == "__main__":
    print("Welcome to the Band Name Generator!\n")
    
    # Taking input from the user
    user_name = input("Enter your name: ").strip()
    city = input("Enter your city: ").strip()

    # Generate and display the band name
    band_name = generate_band_name(user_name, city)
    print("\n🎸 Your awesome band name is: 🎶")
    # print(f"\033[1;32;40m{band_name}\033[0m")  # Output the band name in green color for extra flair
    print(f"{band_name}\n")
    """\033: This is the escape character, which signals that a control sequence is about to follow.

[1;32;40m: This is the sequence that defines the text formatting and color:

1: This makes the text bold.
32: This sets the text color to green.
40: This sets the background color to black.
m : sequence terminator

So, when you use \033[1;32;40m, you're telling the terminal to print the following text in bold green with a black background.

To reset the formatting back to normal, we use the reset code \033[0m, which is included at the end of the string (\033[0m) in the code"""
print("Given by prithvesh")