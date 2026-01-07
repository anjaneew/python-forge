# input() - prompts user input
#           input is a string

name = input("What's your name? ")
age = input("How old are you? ")

# Method 1 : seperate type casting
age = int(age)
age += 1 

# Method 2 : typecasting with input
distance = int(input("How many km to your home ?")) + 5


print(f"hi, {name}. This year you will be {age}. You are {distance} away from home.")

#Exercise - area of a rectangle

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = length * width

print(f"The area of the rectangle is {area} cm²")