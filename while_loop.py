#Exercise 1

name = input("Enter your name: ")

while name == "":
    print("No")
    name = input("Enter your name: ")

print(f"Hello, {name}")

age = int(input("Enter age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter age: "))


# print(f"Hello, {name}, you are {age} years old").

food = input("Enter food name: (q to quit) ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter food name: (q to quit) ")

print("Thank you.")    

#logical operator to while loop

num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"your {num} is invalid.")
    num = int(input("Enter a number between 1-10: "))

print(f"Success! Your number is {num}")    