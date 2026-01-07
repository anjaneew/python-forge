#Python Calculator

# get user input
operator = input("Enter the arithmentic operator: (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#if statement for calculation
if operator == '+':
    result = num1 + num2
    print(f"You asked what is the answer to {num1} {operator} {num2}")
    print(f"The result is {result}")
elif operator == '-':
    result = num1 - num2
    print(f"You asked what is the answer to {num1} {operator} {num2}")
    print(f"The result is {result}")
elif operator == '*':
    result = num1 - num2
    print(f"You asked what is the answer to {num1} {operator} {num2}")
    print(f"The result is {result}")
elif operator == '/':
    result = num1 / num2
    print(f"You asked what is the answer to {num1} {operator} {num2}")
    print(f"The result is {result}")    
else:
    print("We cannot read your input. sorry. Try again.")