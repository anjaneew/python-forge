# dictionary = collection of {key:value} pairs
#            ordered, changable, no duplicates

capitals = {"USA" : "DC", "India": "New Delhi", "China": "Beijing"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("China")) # Beijing or none

if capitals.get("Japan"): # That capital is not listed
    print("That capital is listed.") 
else:
    print("That capital is not listed")

capitals.update({"Sri Lanka": "Colombo"}) # add new
capitals.update({"India": "Mumbai"}) # change 
print(capitals) 
{'USA': 'DC', 'India': 'Mumbai', 'China': 'Beijing', 'Sri Lanka': 'Colombo'}

capitals.pop("China") #remove that item
print(capitals) # {'USA': 'DC', 'India': 'Mumbai', 'Sri Lanka': 'Colombo'}

capitals.popitem() #remove the latest item
print(capitals) # {'USA': 'DC', 'India': 'Mumbai'}

# capitals.clear()
# print(capitals) # {}

# keys value objects 

keys = capitals.keys() # dict_keys(['USA', 'India', 'China'])
print(keys)

values = capitals.values()
print(values) # dict_values(['DC', 'New Delhi', 'Beijing'])

# # items - 2D list
items = capitals.items() 
print(items) #dict_items([('USA', 'DC'), ('India', 'New Delhi'), ('China', 'Beijing')])

for key2, value2 in items:
    print(f"{key2} --> {value2}")

        # USA --> DC
        # India --> Mumbai