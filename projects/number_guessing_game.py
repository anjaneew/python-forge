# Number guessing game
import random

low = 1
high = 10
answer = random.randint(low,high)
guesses = 0
is_running = True

print("----------------------------")
print("-------Guessing Game------")
print(f"Guess a number between {low} and {high}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        # pass
        guess = int(guess)
        guesses += 1
        if guess > high:
            print("Your guess is higher than the range")
        elif guess < low:
            print("Your guess is lower than the range") 
        elif guess == answer:
            print()
            print("You win")
            print(f"Your answer is correct. The number is {answer}. It took you {guesses} guesses") 
            print()
            is_running = False
        else:
            print("Try again")         
    else:
        print("Invalid guess")