import random

# ASCII Logo for Blackjack
logo = '''
  ____  _            _    _            _      _       
 | __ )(_) __ _ _ __| | _(_) ___ _ __ (_) ___| |_ ___ 
 |  _ \| |/ _` | '__| |/ / |/ _ \ '_ \| |/ _ \ __/ _ \\
 | |_) | | (_| | |  |   <| |  __/ | | | |  __/ ||  __/
 |____/|_|\__,_|_|  |_|\_\_|\___|_| |_|_|\___|\__\___|
                                                        
'''

# Card deck setup
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Function to initialize deck
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# Function to calculate score
def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        score += values[rank]
        if rank == 'A':
            ace_count += 1
    # Adjust for Aces
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

# Function to show hand
def show_hand(player, hand):
    print(f"{player}'s hand: {', '.join([card[0] + ' of ' + card[1] for card in hand])} - Score: {calculate_score(hand)}")

# Function to check if the player has Blackjack
def check_blackjack(hand):
    return calculate_score(hand) == 21 and len(hand) == 2

# Function to handle basic, medium, or expert difficulty (affects number of decks)
def choose_difficulty():
    print("Choose your difficulty level:")
    print("1. Basic")
    print("2. Medium")
    print("3. Expert")
    
    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        return 1  # Basic: 1 deck
    elif choice == '2':
        return 2  # Medium: 2 decks
    else:
        return 4  # Expert: 4 decks

# Main game function
def play_game():
    print(logo)
    difficulty = choose_difficulty()
    
    # Create a deck of cards based on the chosen difficulty
    deck = create_deck() * difficulty  # Multiplying the deck for difficulty

    # Deal initial hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Show initial hands
    show_hand("Player", player_hand)
    print(f"Dealer's hand: {dealer_hand[0][0]} of {dealer_hand[0][1]}, Unknown card")
    
    # Check for Blackjack
    if check_blackjack(player_hand):
        print("Blackjack! You win!")
        return
    if check_blackjack(dealer_hand):
        print("Dealer has Blackjack! Dealer wins!")
        return
    
    # Player's turn
    while True:
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        
        if choice == 'hit':
            player_hand.append(deck.pop())
            show_hand("Player", player_hand)
            if calculate_score(player_hand) > 21:
                print("You busted! Dealer wins!")
                return
        elif choice == 'stand':
            break
        else:
            print("Invalid choice. Please choose 'hit' or 'stand'.")
    
    # Dealer's turn
    show_hand("Dealer", dealer_hand)
    while calculate_score(dealer_hand) < 17:
        print("Dealer hits.")
        dealer_hand.append(deck.pop())
        show_hand("Dealer", dealer_hand)
        if calculate_score(dealer_hand) > 21:
            print("Dealer busted! You win!")
            return
    
    # Final results
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    if player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game and ask if the user wants to play again
def main():
    while True:
        play_game()
        choose = input("Do you want to play again (y/n): ").lower()
        if choose != 'y':
            print("Thanks for playing!")
            break

# Run the main loop
main()
