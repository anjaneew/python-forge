'''
Collection = single variable used to store multiple values

List = [] ordered and changable - duplicates are OK - like JS array
set = {} unordered and immutable - Add/Remove OK - no duplicates - like JS set
Tuple = () ordered and unchangeable - duplicates OK - Faster
'''

fruits = ["apple 🍎", "orange 🍊", "banana 🍌", "mango 🥭", "pineapple 🍍"]

print(fruits) #['apple 🍎', 'orange 🍊', 'banana 🍌', 'mango 🥭', 'pineapple 🍍']

print(fruits[1]) #orange 🍊

#range
print(fruits[0:3]) # ['apple 🍎', 'orange 🍊', 'banana 🍌']

#every second
print(fruits[::2]) #['apple 🍎', 'banana 🍌', 'pineapple 🍍']

#reverse
print(fruits[::-1]) # ['pineapple 🍍', 'mango 🥭', 'banana 🍌', 'orange 🍊', 'apple 🍎']

## iterate over the list items
# for fruit in fruits:
#     print(fruit)

# #all the functions to run with a collection
# print(dir(fruits))

'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 
'''

# print(help(fruits)) # all details

#length
print(len(fruits)) # 5

# if this is in the collection
print("apple 🍎" in fruits) #True
print("grape 🍇" in fruits) #False

print(fruits)

#reassigned
fruits[2] = "grape 🍇" #reassignmed

print(fruits)


#append - add an element at the end
fruits.append("banana 🍌")
print(fruits) # ['apple 🍎', 'orange 🍊', 'banana 🍌', 'mango 🥭', 'pineapple 🍍', 'banana 🍌']


#remove - remove the first occurence of it
fruits.remove("banana 🍌")
print(fruits) # ['apple 🍎', 'orange 🍊', 'mango 🥭', 'pineapple 🍍', 'banana 🍌']

#insert - insert at a given index
fruits.insert(2, "grape 🍇")
print(fruits) # ['apple 🍎', 'orange 🍊', 'grape 🍇', 'mango 🥭', 'pineapple 🍍', 'banana 🍌']

fruits.sort()
print(fruits) # ['apple 🍎', 'banana 🍌', 'grape 🍇', 'mango 🥭', 'orange 🍊', 'pineapple 🍍']

fruits.reverse() # ['pineapple 🍍', 'orange 🍊', 'mango 🥭', 'grape 🍇', 'banana 🍌', 'apple 🍎']
print(fruits)

# # fruits.clear() # []
# # print(fruits)

# which index
print(fruits.index("apple 🍎")) #0
# print(fruits.index("coconut ")) # give an error -> ValueError: 'coconut ' is not in list

print(fruits.count("mango 🥭")) # 1 (if none 0)

#----------------SET--------------------------

'''
useful for constants like colors
'''

animals = {"🐕","🐈","🐂","🐄","🐁","🐕", "🐂", "🐂", "🐂", "🐂"}
print(animals) # {'🐂', '🐈', '🐄', '🐕', '🐁'} - no duplicates - unordered so they change each time

# print(dir(animals))
# print(help(animals))

print(len(animals)) # 5

print("🐈" in animals) # True

# #cant do indexing 
# print(animals[1]) # TypeError: 'set' object is not subscriptable

animals.add("🐘")
print(animals) # {'🐁', '🐕', '🐂', '🐄', '🐘', '🐈'}

animals.remove("🐁")
print(animals) # {'🐕', '🐄', '🐘', '🐂', '🐈'}

animals.pop() # removes first - but its random
print(animals) #{'🐄', '🐂', '🐕', '🐘'}

animals.clear() 
print(animals) # set()

#-------------- Tuple() ----------------

places = ("🏛️","🏗️","🏠","🏠","🏢","🏣","🏪","🏩","🏦","🏥","🏤","🏨")
print(places)

print(len(places)) #12
print("🏥" in places) # True
print(places.index("🏥")) # 9
print(places.count("🏠")) # 2

for place in places:
    print(place)

