class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def read(self):
        print(f"You are reading {self.title} by {self.author} published in {self.year}.")
