# from script2 import *
#                   * = everything
# print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
'''

# print(__name__) # script2
# #                 __main__

def favourite_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("This is script 1")
    favourite_food("parippu")
    print("Goodbye !")

#if this block is missing, the file will always
#  run main in any import
if __name__ == '__main__':
    main()    