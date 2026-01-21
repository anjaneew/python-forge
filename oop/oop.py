from book import Book

# Python Object Oriented Programming

# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex: phone, cup, book
#          You need a class to create many objects

# class  = (blueprint) used to design the structure and layout of an object

#creating car object
class Car:       # self - this object we are creating                                     
     def __init__(self, model, year, color, for_sale): #constructor method
          self.model = model
#This objects model is what passed in as the model
          self.year =  year
          self.color = color
          self.for_sale = for_sale

#    methods
     def drive(self):
          print(f"You drive the {self.model}. 🚗💨")     

car1 = Car("BMW", 2026, "black", False)
car2 = Car("Corvette", 2025, "blue", True)

print(car1) # memory address - <__main__.Car object at 0x72de224e7110>

#         . attribute access operator
print(car1.model) # BMW
print(car2.color) # blue



# this is ineffective way to store. so better save class in a seperate file. 
# from book import Book 

book1 = Book("Robin Hood", "Aston", 1515)


print(f"Book: {book1.title}\nAuthor: {book1.author}\nYear: {book1.year}")
'''
Book: Robin Hood
Author: Aston
Year: 1515
'''

# methods
car1.drive() # You drive the BMW. 🚗💨
book1.read() # You are reading Robin Hood by Aston published in 1515.