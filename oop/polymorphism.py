# Polimorphism = Greek word - "to have many forms or faces"

#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance -> an object could be treated of the same type as a parent class
#               2. "Duck typing"-> Object must have necessary attributes/methods

#               1. Inheritance

from abc import ABC, abstractmethod #importing abstract classes

class Shape:

    @abstractmethod # decorator of abstract method
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2   

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2 

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5    
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
    



circle = Circle(45) # Circle is a circle and a shape

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("mushroom", 15)]

for shape in shapes:
    print(f"The area is {shape.area()}cm².") # Alt + 0178

'''
The area is 50.24cm².
The area is 25cm².
The area is 21.0cm².
The area is 706.5cm².
'''    