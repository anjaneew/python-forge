#Python slot machine
import random

#spin
def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']
    

    # #old fashion for loop
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results   

    # list comprehension 
    
    return [random.choice(symbols) for _ in range(3)]

#display
def print_row():
    pass

#payout
def get_payout():
    pass

#main 
def main():
    balance = 100
    print()
    print("Welcome to Python slot")
    print()
    print("Symbols: 🍒🍉🍋🔔⭐")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        #input validation

        if not bet.isdigit():
            print("Please enter a valid number: ")
            continue #this will skip the current itteration and start from the begining

        bet = int(bet)

        if bet > balance:
            print("Insufficent funds.") 
            continue  

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet    
        row = spin_row()


if __name__ == '__main__':
    main()