foods = []
prices = []
total = 0

while True: 
    food = input("Enter food: (press 'q' to quit): ")
    

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price for {food}: (press 'q' to quit): "))
        foods.append(food)
        prices.append(price)

print("------------ YOUR CART  ------------")
for item in foods:
    for cost in prices:
        print("", end=" ")
    print(f"{item} ---- ${cost}")
    total += cost    
print("", end=" ")
print(f"Total  ---- ${total}")