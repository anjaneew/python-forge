class Backery:

    # class variables
    cupcake_count = 0

    # constructor
    def __init__(self, flavor, topping):
        self.flavor = flavor
        self.topping = topping
        Backery.cupcake_count += 1

    #instance method
    def ready_order(self):
        return f"Your {self.flavor} flavored cupcake with {self.topping} topping is ready! 🧁"

    # class method
    @classmethod
    def get_inventory(cls):
        return f"We have {cls.cupcake_count}s cupcakes 🧁 in store."    
    
    #static method
    @staticmethod
    def is_valid_order(order_flavor, order_topping):
        flavors_list = ["chocolate", "vanilla", "strawberry", "red velvet", "lemon", "banana", "coffee"]
        toppings_list = ["chocolate","buttercream", "sprinkles", "fruits", "nuts", "candy"]

        if order_flavor in flavors_list and order_topping in toppings_list:
            return f"Your {order_flavor} with {order_topping} will be ready. Please wait.✅"
        else:
            Backery.display_menu()
            return f"Your {order_flavor} with {order_topping} is not available. Please choose again"


    #static method
    @staticmethod
    def display_menu():
        flavors_list = ["chocolate", "vanilla", "strawberry", "red velvet", "lemon", "banana", "coffee"]
        toppings_list = ["chocolate","buttercream", "sprinkles", "fruits", "nuts", "candy"]
        
        print()
        print("*******Menu*******")
        for flavor in flavors_list:
            print(f"Flavors: {flavor}")
        for topping in toppings_list:
                print(f"Toppings: {topping}")
        print()


# creating instances

print(Backery.is_valid_order("pinapple", "peppermint"))
print(Backery.is_valid_order("vanilla", "peppermint"))

print(Backery.get_inventory()) # We have 0s cupcakes 🧁 in store.

order1 = Backery("chocolate", "buttercream")  
order2 = Backery("vanilla", "sprinkles") 
order3 = Backery("coffee", "nuts") 
order4 = Backery("red velvet", "fruits") 

print(Backery.get_inventory()) # We have 4s cupcakes 🧁 in store.

print(order1.ready_order()) # Your chocolate flavored cupcake with buttercream topping is ready! 🧁
print(order2.ready_order()) # Your vanilla flavored cupcake with sprinkles topping is ready! 🧁
print(order3.ready_order()) # Your coffee flavored cupcake with nuts topping is ready! 🧁
print(order4.ready_order()) # Your red velvet flavored cupcake with fruits topping is ready! 🧁

'''

*******Menu*******
Flavors: chocolate
Flavors: vanilla
Flavors: strawberry
Flavors: red velvet
Flavors: lemon
Flavors: banana
Flavors: coffee
Toppings: chocolate
Toppings: buttercream
Toppings: sprinkles
Toppings: fruits
Toppings: nuts
Toppings: candy

Your pinapple with peppermint is not available. Please choose again

*******Menu*******
Flavors: chocolate
Flavors: vanilla
Flavors: strawberry
Flavors: red velvet
Flavors: lemon
Flavors: banana
Flavors: coffee
Toppings: chocolate
Toppings: buttercream
Toppings: sprinkles
Toppings: fruits
Toppings: nuts
Toppings: candy

Your vanilla with peppermint is not available. Please choose again
We have 0s cupcakes 🧁 in store.
We have 4s cupcakes 🧁 in store.
Your chocolate cupcake with buttercream is ready! 🧁
Your vanilla cupcake with sprinkles is ready! 🧁
Your coffee cupcake with nuts is ready! 🧁
Your red velvet cupcake with fruits is ready! 🧁
'''





