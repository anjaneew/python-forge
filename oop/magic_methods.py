# Magic Methods = Dunder Methods (double underscore) 
#                 __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behaviour of objects


class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)

print(student1) # name: Spongebob gpa: 3.2
print(student1 == student2) # False - equal or not
print(student1 > student2) # True - greater than or less than

#--------------------------------------------------------------

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return f" {self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title 
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"{key} was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)

print(book1) # The Hobbit by J.R.R. Tolkien
print(book2) # Harry Potter and The Philosopher's Stone by J.K. Rowling
print(book3) # The Lion, The Witch and the Wardrobe by C.S. Lewis

# print(book1 == book2) # False - without __eq__ it will always say false
print(book1 == book4) # True

# __gt__ greater than / less than
print(book1 > book2) # greater than - True 
print(book3 < book2) # less than - True

# __add__
print(book1 + book2) #  533

# contains
print("Lion" in book3) # True

# get item
print(book1['title']) #The Hobbit