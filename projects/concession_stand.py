# concession stand

#dictionary
menu = { "coke" : 1.99,
        "chips" : 0.60,
        "popcorn" : 6.00,
        "soda" : 0.85,
        "lemonade" : 1.30,
        }

#user input
cart = []

total = 0


print("--------------MENU--------------")

for key2, value2 in menu.items():
    print(f"{key2:10} ----> ${value2}")

print("----------------------------")

print()

while True:
    choice = input("Select item: (q to quit) ").lower()

    if choice == "q":
        break
    elif menu.get(choice) is not None:
        cart.append(choice)
        new_item = float(menu.get(choice.lower()))
        total += new_item

#output
print() 
print("-----------Your cart-----------------") 
for food in cart:
    print(f"{food:10} ----> ${menu.get(food)}")  
print("----------------------------")          
print(f"The total is ${total}")
print("----------------------------")  