# format specifiers = {value:flag}
#                      format a value based on the flags inserted
#
#  .(number)f --> round to decimal places (fixed point)
#
#  :(number)  --> allocate that many spaces 
#
#  :03        --> allocate and zero pad that many spaces
#
# : <   left justify
# : >   right justify
# : ^   center align
# : + use a plus sign to indicate positive value
# : = place sign to leftmost position
# :   insert a space before positive numbers
# :,  comma seperator
#


price1 = 365879.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1: {price1}") 
print(f"Price 2: {price2}") 
print(f"Price 3: {price3}") 

#  .(number)f --> round to decimal places (fixed point)

print(f"Price 1: {price1:.2f}") #Price 1: 3.14
print(f"Price 2: {price2:.2f}") #Price 2: -987.65
print(f"Price 3: {price3:.2f}") #Price 3: 12.34

#  :(number)  --> allocate that many spaces 

print(f"Price 1: {price1:10}") #Price 1:    3.14159
print(f"Price 2: {price2:10}") #Price 2:    -987.65
print(f"Price 3: {price3:10}") #Price 3:      12.34

#  :03        --> allocate and zero pad that many spaces

print(f"Price 1: {price1:010}") #Price 1: 0003.14159
print(f"Price 2: {price2:010}") #Price 2: -000987.65
print(f"Price 3: {price3:010}") #Price 3: 0000012.34

# justify

# :< left

print(f"Price 1: {price1:<10}") #Price 1: 3.14159
print(f"Price 2: {price2:<10}") #Price 2: -987.65
print(f"Price 3: {price3:<10}") #Price 3: 12.34

# :> right

print(f"Price 1: {price1:>10}") #Price 1:    3.14159
print(f"Price 2: {price2:>10}") #Price 2:    -987.65
print(f"Price 3: {price3:>10}") #Price 3:      12.34

# :^ center

print(f"Price 1: {price1:^10}") #Price 1:  3.14159 
print(f"Price 2: {price2:^10}") #Price 2:  -987.65
print(f"Price 3: {price3:^10}") #Price 3:   12.34

# :+ for positive values
print(f"Price 1: {price1:+}") #Price 1: +3.14159
print(f"Price 2: {price2:+}") #Price 2: -987.65
print(f"Price 3: {price3:+}") #Price 3: +12.34

# :   insert a space before positive numbers
print(f"Price 1: {price1: }") #Price 1:  365879.14159
print(f"Price 2: {price2: }") #Price 2: -987.65
print(f"Price 3: {price3: }") #Price 3:  12.34


# :,  Thousand seperator - comma seperator
print(f"Price 1: {price1:,}") #Price 1: 365,879.14159
print(f"Price 2: {price2:,}") #Price 2: -987.65
print(f"Price 3: {price3:,}") #Price 3: 12.34


# print(f"Price 1: {price1}") #
# print(f"Price 2: {price2}") #
# print(f"Price 3: {price3}") #
