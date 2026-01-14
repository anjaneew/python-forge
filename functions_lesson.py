# function - reusable code
# return statement 

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("robin", "hood")

print(full_name)