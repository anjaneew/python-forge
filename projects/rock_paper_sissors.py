import random

options = ("rock", "paper", "sissors")

is_playing = True

while is_playing:
    print()
    print("----------Game Play----------")
    player = None
    computer = random.choice(options)

    while player not in options: 
        player = input("Enter your choice(rock, paper, sissors): ")
    print()
    print(f"The player's choice: {player}")
    print(f"The computer's choice: {computer}")
    print()

    if (player == "rock" and computer == "sissors") or (player == "paper" and computer == "rock") or (player ==  "sissors" and computer == "paper"):
        print("You win!")
        
    elif player == computer:
        print("Tie!")     
    else:
        print("You lose!")     

    play_again = input("Play again? (y/n) ").lower() 

    if not play_again == "y":
        is_playing = False    
print()  
print("Thanks for playing!")        