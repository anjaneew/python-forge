# Membership operators = test if a value/varable is found in 
#                           a sequence (string, list, tuple, set,   
#                           dictionary) 
#   - in   - not in

#Example 1
word = "apple"

letter = input("Guess a letter: ")

if letter not in word: # case sensitive
    print(f"{letter} is not found in the secret word.")
else:
    print(f"{letter} is found in the secret word.")


#Example 2

suspects = { "Robin", "Marion" , "March"}

suspect = input("Enter the suspect: ")

if suspect in suspects:
    print(f"{suspect} is the criminal.")
else:
    print(f"{suspect} is innocent.")   