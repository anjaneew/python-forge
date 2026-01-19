#Variables

#data-types - string, integer, float, boolean

myhouse = "Malwana"
family = 5
price = 9800.85
isResident = False

#f-strings

print(f"I am from {myhouse}. It is now worth ${price}. We have {family} members. But is it my current residence? {isResident}")

isStudent = True

#If statements:

if isStudent:
    print("I am a student.")
else:
    print("I am not a student.")    

#multiple variables 
 
#  'Hello World', to 3 variables 

x = y = z = "Hello World"
print(x) #Hello World
print(y) #Hello World
print(z) #Hello World

# values to multiple variables in one line

x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry