import random

#getting a random number within a range
high = 6
low = 1
dice = random.randint(low, high)
print(dice)

# random floating point number
num = random.random()
print(f"{num:.2f}") # format specifiers only work in fstrings

#random choices
options = ("rock", "paper", "sissors")
mychoice = random.choice(options)
print(mychoice)

card_deck = [ "A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
    "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
    "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
    "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"  ]
#shuffling deck
random.shuffle(card_deck)
print(card_deck)
# random card
card = random.choice(card_deck)
print(card)