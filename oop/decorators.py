# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

# Example

#             @add_sprinkles  - decorator
#             get_ice_cream("vanilla") - base function

# wrapper makes sure this runs only when we call the funtion , not always
# -----------------------------------------------------------

# Formula to creating a decorator
def add_sprinkles(func):
    def wrapper(*args, **kwargs): 
        print("You add sprinkles 🍨")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper    

@add_sprinkles 
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla") 
# You add sprinkles 🍨 
# You add fudge 🍫
# Here is your vanilla ice cream 🍦