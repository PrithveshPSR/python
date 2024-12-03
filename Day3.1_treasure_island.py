def treasure_island():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    
    # First choice: Left or Right
    first_choice = input("Left or Right? ").lower()
    
    if first_choice == "left":
        # Second choice: Wait or Swim
        second_choice = input("Wait or Swim? ").lower()
        
        if second_choice == "swim":
            print("Attacked by trout.")
            print("Game Over.")
        else:
            # Third choice: Which door? Blue, Yellow, Red
            door_choice = input("Which door? Blue, Yellow, Red ").lower()
            
            if door_choice == "blue":
                print("Eaten by beasts.")
                print("Game Over.")
            elif door_choice == "yellow":
                print("You Win!")
            elif door_choice == "red":
                print("Burned by fire.")
                print("Game Over.")
            else:
                print("Invalid choice.")
                print("Game Over.")
    
    elif first_choice == "right":
        print("Fall into a hole.")
        print("Game Over.")
    
    else:
        print("Invalid choice.")
        print("Game Over.")

# Start the game
treasure_island()
