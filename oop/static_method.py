# Static Method = A method that belongs to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position 

    # instance method
    def get_info(self):
        return f"{self.name} : {self.position}"   
    
    # static method
    @staticmethod 
    def is_valid_position(position):
        valid_positions = ["manager", "cashier", "cook", "janitor"]
        return position in valid_positions


employee1 = Employee("Merwin Silva", "Janitor")
print(employee1.get_info()) # Merwin Silva : Janiter

print(Employee.is_valid_position("janitor")) # True