# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle: 

    def __init__(self, width, height):
        self._width = width   #_ makes it private - internal - 
        self._height = height # these values are not meant to be accessed directly

    @property # anyone needing width are supposed to get it using these (getters and setters)
    def width(self): 
        return f"{self._width:.1f} cm"   # additional logic

    @property
    def height(self):
        return f"{self._height:.1f} cm"   
    
    @width.setter  # additional logic when setting
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero.")   

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero.")       

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle1 = Rectangle(3, 4)
rectangle1.height = 0 # Height must be greater than zero.

print(f"Width: {rectangle1.width} Height: {rectangle1.height}" ) # Width: 3.0 cm Height: 4.0 cm

del rectangle1.width #Width has been deleted
del rectangle1.height #Height has been deleted

