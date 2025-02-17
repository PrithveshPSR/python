import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the logo from art.py (assuming art is a valid module that can show a logo)
print("Auction")

# Dictionary to store bids
bids = {}

# Main loop to collect bids
while True:
    # Ask for the user's name
    name = input("What is your name? ")

    # Ask for the bid price
    bid_price = float(input("What is your bid price? $"))

    # Add the name and bid to the dictionary
    bids[name] = bid_price

    # Ask if there are other users who want to bid
    more_bids = input("Are there other users who want to bid? (yes/no): ").lower()

    if more_bids != "yes":
        break

    # Clear the screen for the next bid
    clear_screen()

# Find the highest bid and declare the winner
if bids:
    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of ${bids[winner]:.2f}")
else:
    print("No bids were placed.")