# # *args   --> allow you to pass multiple non-key arguments
# # **kwargs --> allow you to pass multiple keyword arguments
# #       * --> unpacking operator
# # ( argument types ) : 
# #   1. positional 2. default 3. keyword 4. arbitrary

# # Example 1: V1 
# def add(a, b):
#     return a + b

# result1 = add(1, 2)
# print(result1)

# # Example 1: V2 arbitrary arguments use
# def add2(*args):
#     print(type(args)) # <class 'tuple'> - so we can use those methods
#     total = 0
#     for arg in args: # or num in nums (any word is ok)
#         total += arg
#     return total    

# result2 = add2(1, 2, 4, 5) #12
# print(result2)


# # Example 2: arbitrary arguments use
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")   
# #             Dr. Spongebob Harold Squarepants III      


# # Example 3: V1 keyword arguments use
# def print_address(**kwargs):
#     print(type(kwargs)) # <class 'dict'>
#     print()
#     for key, value in kwargs.items():
#         print(f"{key:10}: {value}")
#     print()


# print_address(street="123 Fake St.", city="Detroit", state="MI", zip="54321")

# Example 4:V1 arbitrary & keyword arguments use
def shipping_label(*args, **kwargs):
    print()
    for arg in args:
        print(arg, end=" ")
    print()    
    for value in kwargs.values():
        print(value, end=" ") 
    print()   


shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III", street="123 Fake St.", city="Detroit", state="MI", zip="54321")

# Dr. Spongebob Harold Squarepants III 
# 123 Fake St. Detroit MI 54321 

# Example 4:V2 arbitrary & keyword arguments use
def shipping_label(*args, **kwargs):
    print()
    for arg in args:
        print(arg, end=" ")
    print()    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apt')},")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')},")
        print(f"{kwargs.get('pobox')},")  
    else:
        print(f"{kwargs.get('street')},")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}.")    
    print()   


shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III", street="123 Fake St.", pobox="PO box #0182", city="Detroit", state="MI", zip="54321")

# Dr. Spongebob Harold Squarepants III 
# 123 Fake St.,
# Detroit, MI, 54321.

# Dr. Spongebob Harold Squarepants III 
# 123 Fake St., 203,
# Detroit, MI, 54321.

# Dr. Spongebob Harold Squarepants III 
# 123 Fake St.,
# PO box #0182,
# Detroit, MI, 54321.
