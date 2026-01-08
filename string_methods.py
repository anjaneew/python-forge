# # string methods

# name = input("Name? ")
# contact = input("Contact number: ")

# # length function
# result1 = len(name) 
# print(f"The length of the {name} is {result1}characters.")

# # find - 1st occurence
# result2 = name.find("A") 
# print(f"The first occurence of 'A'  is {result2} character position.")

# # rfind - reverse 1st occurence
# result3 = name.rfind(" ") 
# print(f"The last occurence of ' '  is {result3} character position.")


# result4 = name.isdigit()
# print(result4)
# result5 = name.isalpha()
# print(result5)
# result6 = contact.count('-')
# print(result6)
# result7 = contact.replace('-', ' ')
# print(result7)

# #get all string methods
# print(help(str))

# Exercise: Validate input
print("Instructions: username must be 12 characters ling, no spaces, no digits.")

username = input("Enter username: ")

char_count = len(username)
has_space = if (username.find(" ") ==  -1) == "True" else "False"
has_digits = username.isdigit()