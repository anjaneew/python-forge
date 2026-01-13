import time

# nested loop

# outer loop:
#   inner loop:

# #my version
# for x in range(1,11):
#     for y in range(1,4):
#         time.sleep(3)
#         print(f"person {x} is getting package {y}.")


# #infinte loops
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))

# # While loop inside a while loop
# while x > 0:
#     while y > 0:
#         print("While loop inside a while loop")

# # for loop inside a while loop
# while x > 0:
#     for y in range (9):
#         print("for loop inside a while loop")

# # While loop inside a for loop
# for x in range(3):
#     while y > 0:
#         print("While loop inside a for loop")

# # for loop inside a for loop
# for x in range(3):
#     for y in range (9):
#         print("for loop inside a for loop")

# Exercise 1
# for x in range(3):
#     for y in range(1,10):
#         print(y, end=" ")
#     print()    

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol you want: ")    

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print(" ")    