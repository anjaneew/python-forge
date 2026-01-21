# Inheritance = Allows a class to inherit attributes and methods from other class 
#               Helps with code reusability and extensibility
#               class Child(Parent)
#                      sub  (super)

#Example
class Father:
    height = 182
    color = "pink"

class Son(Father):
    pass    

#Example 2

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")    


class Dog(Animal):
    def __init__(self, name, has_tail):
        super().__init__(name)
        self.has_tail = has_tail

    def bark(self):
        print(f"{self.name} goes BAW BAW BAW! 🐕")    

dog = Dog("Boola", True)
print(dog.name) #Boola
dog.eat() #Boola is eating.
dog.bark() #Boola goes BAW BAW BAW! 🐕
