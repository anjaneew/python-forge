# Class variables = shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Cupcake:

    counter = 0 # class variables

    def __init__(self, color, taste):
        self.color = color    # instance variables
        self.taste = taste    # instance variables
        Cupcake.counter += 1 # access by class not self

cupcake1 = Cupcake("red", "icing")
cupcake1 = Cupcake("blue", "chocolate")

print(cupcake1.color) # blue
print(Cupcake.counter) # 2 - access by class not instance