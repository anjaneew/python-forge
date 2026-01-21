# multiple inheritance = inherit from more than one parent class
#                        C(A, B)
#
# multilevel inheritance = inherit from a parent which inherits from another parent
#                        C(B) <- B(A) <- A

#multilevel inheritance
class Animal:
    def __init__(self):
        self.is_alive = True

    def eat(self):
        print("He is eating. 🍒🍉🍈🍇🍖🌿🍃🥬")    

class Prey(Animal):
    def __init__(self, name):
        Animal.__init__(self) #not super cz multiple stuff confusing
        self.name = name

    def flee(self):
        print(f"{self.name} is fleeing. 💀")

class Preditor(Animal):
    def __init__(self, name):
        Animal.__init__(self) #not super cz multiple stuff confusing
        self.name = name

    def hunt(self):
        print(f"{self.name} is hunting. 🩸")


class Rabbit(Prey):
    pass

class Hawk(Preditor):
    pass

#multiple inheritance
class Fish(Prey, Preditor):
    def __init__(self, name):
        Prey.__init__(self, name)
        Preditor.__init__(self, name)


fish = Fish("Shark")
print(fish.name) # Shark
print(fish.is_alive)
fish.flee() # Shark is fleeing. 💀
fish.hunt() # Shark is hunting. 🩸
fish.eat() # He is eating. 🍒🍉🍈🍇🍖🌿🍃🥬
