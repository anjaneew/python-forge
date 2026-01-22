# "Duck typing" => 2.nd way to polymorphism 🦆🦆🦆🦆🦆
#                  object must have the minimal necessary attributes/methods
#                  "If it looks like a duck, quacks like a duck, it must be a 🦆"


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof! 🐕")    

class Cat(Animal):
    def speak(self):
        print("Gnaaw! 🐈")   

# sample duck typing
class Car:
    # def horn(self):
    #     print("Broom! 🚗")     # doesnt have minimal necessary attributes/methods   
    # 
    alive = False

    def speak(self):
        print("Broom! 🚗")   


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(f"Alive: {animal.alive}")
'''
Woof! 🐕
Alive: True
Gnaaw! 🐈
Alive: True
Broom! 🚗
Alive: False
'''    

