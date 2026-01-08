"""
If Conditional Statement

example : 
            age = 20
            if age >= 18:
                print("Eligible to vote.")

Short Hand if

example : 
            age = 19
            if age > 18: print("Eligible to Vote.")

If else Conditional Statement

example : 
            age = 10
            if age <= 12:
                print("Travel for free.")
            else:
                print("Pay for ticket.")

Short Hand if-else

example : 
            marks = 45
            res = "Pass" if marks >= 40 else "Fail"
            print(f"Result: {res}")

elif Statement

example : 
    age = 25

    if age <= 12:
        print("Child.")
    elif age <= 19:
        print("Teenager.")
    elif age <= 35:
        print("Young adult.")
    else:
        print("Adult.")

Ternary Conditional Statement
      X if condition else Y

example : 

    # Assign a value based on a condition
    age = 20
    s = "Adult" if age >= 18 else "Minor"
    print(s)

"""


# Exercise:

response = input("Are you hungry? (Y/N): ")

# if response == "Y" :
#     print("Here is some food.")

# elif response == "N":
#     print("Then you can have some refreshing drink.")

# else: 
#     print("We cannot read your response. ")    

print("Here is some food.") if response ==   "Y" else   print("Then you can have some refreshing drink.")