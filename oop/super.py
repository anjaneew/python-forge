#super() = Function used in a child class to call methods 
#          from a parent class (super class) 
#          Allows you to extend the funtionality of the inherited methods

# Example - overlapping attributes
'''
class Circle:
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius

class Square:
    def __init__(self, color, filled, width):
        self.color = color
        self.filled = filled
        self.width = width        

class Triangle:
    def __init__(self, color, filled, width, height):
        self.color = color
        self.filled = filled
        self.width = width
        self.height = height     
'''     

class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe1(self):
        print(f"Describe 1: It is {circle.color} and {'filled' if self.is_filled else 'not filled'}.")    

    def describe2(self): #This method is overwritten
        print(f"Describe 2: It is {circle.color} and {'filled' if self.is_filled else 'not filled'}.")      

    def describe3(self): # Exending functionality of this
        print(f"Describe 3: It is {circle.color} and {'filled' if self.is_filled else 'not filled'}.")      

class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    # Method overriding
    def describe2(self):
        print(f"It is a circle with the area of { 3.14 * self.radius * self.radius} cm ^2")  

    # Extending Functionality
    def describe3(self):
        super().describe3()
        print(f"It is a circle with the area of { 3.14 * self.radius * self.radius} cm ^2")
                
class Square(Shapes):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width        

class Triangle(Shapes):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height 

# keyword arguments - not necessary - good for readabilty
circle = Circle(color="red", is_filled=True, radius=35)   
print(f"The circle is {circle.color} and {circle.is_filled}. It has a radius of {circle.radius}.")  # The circle is red and True. It has a radius of 35.
circle.describe1() # Describe 1: It is red and filled.
circle.describe2() # It is a circle with the area of 3846.5 cm ^2
circle.describe3() # Describe 3: It is red and filled. It is a circle with the area of 3846.5 cm ^2