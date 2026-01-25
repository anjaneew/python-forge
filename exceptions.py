# exception = an event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try  2. except  3. finally

# 1 / 0 # ZeroDivisionError: division by zero

# operations with values of different data types
# 1 + "1" # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# attempt to typecast values of wrong data type
#int("pizza") # ValueError: invalid literal for int() with base 10: 'pizza'

'''
Fomat for exceptions

try:
    #try some code
except Exception:
    # handle an Exception
finally:
    # Do some clean up

BAD PRACTICE TO CATCH ALL EXCEPTIONS:

try:
    #try some code
except Exception: 🙅‍♂️
    print("Something went wrong!") 
finally:
    # Do some clean up       
'''
try: 
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT.")
except  ValueError:
    print("Enter only numbers please.") 
except Exception:
    print("Something went wrong!")          
finally:
    #always run - clean up - close files
    print("Do some clean up here. 🧹")    