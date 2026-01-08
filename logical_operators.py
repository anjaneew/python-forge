# Python Logical Operators

# Operator	        Description	               Example
#
#   and 	   Returns True if both        x < 5 and  x < 10
#              statements are true

#   or         Returns True if one of      x < 5 or x < 4
#              the statements is true

#   not        Reverse the result,         not(x < 5 and x < 10)
#              returns False if the 
#              result is true

temp = float(input("What is the tempreture in Celsius? "))
is_raining = input("Is it raining? True or False: ") == "True" # Compare the string

#bool() doesn't read the meaning of the text. It just checks: "Is there something?" If yes → True.

if temp > 20 and not is_raining:
    print("Event is happening today.")
elif temp < 20 or is_raining:
    print("The weather is not good now. We will check in the evening.")    
else: 
    print("The weather is not good today. We will reschedule.")      