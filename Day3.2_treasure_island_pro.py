import random

def treasure_island():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    
    inventory = []  # List to keep track of the player's inventory
    
    # First choice: Left or Right
    first_choice = input("Left or Right? ").lower()
    
    if first_choice == "left":
        print("You head down a mysterious path to the left.")
        
        # Introduce a random event
        event = random.choice(["find_item", "nothing_happens", "get_attack"])
        if event == "find_item":
            print("You find a mysterious map! You add it to your inventory.")
            inventory.append("Map")
        elif event == "get_attack":
            print("You are attacked by wild animals!")
            if "Map" in inventory:  # If the player has the map, they can escape
                print("You use the map to find a safe path and avoid the animals.")
            else:
                print("Without the map, you are cornered and the animals overwhelm you. Game Over.")
                return
        
        # Second choice: Wait or Swim
        second_choice = input("Wait or Swim? ").lower()
        
        if second_choice == "swim":
            print("You swim across a dangerous river and are attacked by trout.")
            print("Game Over.")
        else:
            print("You wait by the shore and see a figure in the distance. It’s a guide!")
            
            # Introduce a puzzle challenge
            print("The guide offers you a riddle. Answer correctly to continue.")
            answer = input("What has keys but can't open locks? ").lower()
            
            if answer == "piano":
                print("Correct! The guide helps you pass safely.")
            else:
                print("Wrong! The guide leaves you, and you are lost.")
                print("Game Over.")
                return
            
            # Third choice: Which door? Blue, Yellow, Red
            door_choice = input("Which door? Blue, Yellow, Red ").lower()
            
            if door_choice == "blue":
                print("You enter the blue door and are eaten by beasts.")
                print("Game Over.")
            elif door_choice == "yellow":
                print("Congratulations! You find the treasure hidden behind the yellow door.")
                print("You Win!")
            elif door_choice == "red":
                print("The red door leads to a fiery pit. You are burned by fire.")
                print("Game Over.")
            else:
                print("Invalid choice.")
                print("Game Over.")
    
    elif first_choice == "right":
        print("You walk to the right and fall into a deep hole.")
        print("Game Over.")
    
    else:
        print("Invalid choice.")
        print("Game Over.")

# Start the game
treasure_island()