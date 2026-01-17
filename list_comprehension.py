# list comprehension = a consise way to create lists in Python
#                      Compact & easier to read than traditional loops
#                      [expression for value in iterable if condition]

# iterables = thinkks can be iterated over in a loop
#           lists [], sets {} , 

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

triples = [ x * 3 for x in range(1,5)]
print(triples) #[3, 6, 9, 12]



