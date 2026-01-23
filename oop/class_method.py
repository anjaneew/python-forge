# Class Method = Allow operations related to the class itself
#                Take (cls) as the first parameter, which represent class itself.
#                difference: instance methods take (self) as first parameter

class Student:

    count = 0
    total_gpa = 0

    # constructor
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=  1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"Name: {self.name} - GPA: {self.gpa}"    

    # class method that works with class data
    @classmethod
    def get_count(cls):
        return f"Total Number: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.2f}"

#create instances
student1 = Student("Amarabandu Roopasinghe", 4.0)
student2 = Student("Ama", 3.0)
print(student1.get_info()) # Name: Amarabandu Roopasinghe - GPA: 4.0

# call class method
print(Student.get_count()) # Total Number: 1
print(Student.get_average_gpa()) # Average gpa: 3.50