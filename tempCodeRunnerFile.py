# *args   --> allow you to pass multiple non-key arguments
# # *kwargs --> allow you to pass multiple keyword arguments
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