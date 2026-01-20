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
def print_row(row):
    print("************")
    print(" | ".join(row))
    print("************")

#payout
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉': 
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 7
        elif row[0] == '⭐':
            return bet * 10
    return 0        


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
        print("Spinning...\n")
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else: 
            print("Sorry, you lost this round.")    
        balance += payout

        play_again = input("Play again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print(f"Game over! Your final balance is ${balance}")        


if __name__ == '__main__':
    main()