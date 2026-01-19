# list comprehension = a consise way to create lists in Python
#                      Compact & easier to read than traditional loops
#                                                           optional
#                      [expression for value in iterable if condition]

# iterables = thinkks can be iterated over in a loop
#           lists [], sets {} , dictionary { "" : ""}

#--------------------Example--------------------
# traditional loop
doublesI = []

for x in range(1,11):
    doublesI.append(x * 2)

print(doublesI) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# list comprehension use
#         [expression for value in iterable if condition]
doublesII = [x * 2 for x in range(1,11)]

print(doublesII) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#-------------------Exercise ---------------------

triples = [ x * 3 for x in range(1,6)]
print(triples) # [3, 6, 9, 12, 15]

squares = [ x * x for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

#-------------------Exercise - Strings ---------------------

fruits = ["apple", "banana", "orange"]
fruits = [ fruit.upper() for fruit in fruits]

print(fruits) # ['APPLE', 'BANANA', 'ORANGE']

message = "You are the ancestor that changes everything for your bloodline. You are the golden light in human form brought to earth with a higher purpose."

message = [char.upper() for char in message]
print(message)

#-------------------Exercise - Conditions ---------------------

numbers = [ 1, -2, 3, -4, -5]
positive_nums = [num for num in numbers if num >=  0]
print(positive_nums) # [1, 3]
negative_num = [num for num in numbers if num <= 0]
print(negative_num) # [-2, -4, -5]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums) # [-2, -4]
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums) # [1, 3, -5]

grades = [85, 42, 79, 90, 56, 61, 30]
passed_grades = [ grade for grade in grades if grade >= 60]
print(passed_grades) # [85, 79, 90, 61]

student_list = { "Arawinda": 85, "Suni": 42, "Lila": 79, "Yohan": 90, "Mala": 56, "Roshan": 61, "Brain": 30}
passed_students = [ key for key, value in student_list.items() if value >= 60]
print(passed_students) # ['Arawinda', 'Lila', 'Yohan', 'Roshan']
passed_students_list = [ (key, value) for key, value in student_list.items() if value >= 60]
print(passed_students_list) # [('Arawinda', 85), ('Lila', 79), ('Yohan', 90), ('Roshan', 61)]