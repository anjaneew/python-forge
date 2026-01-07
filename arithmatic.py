
import math

# Arithmetic operators
#  
# += plus , -= minus, *= multipication, /= division, 
 # **= (to the power of), % remainder

# Math functions

x = 3.14
y = 4
z = 5

# 1. Round function
result1 = round(85.4923545, 2) # also round(x)
print(result1) # 85.49

#2. Absolute value
result2 = abs(y)
print(result2) #4 even if its -4

#3. Power function
result3 = pow(4, 3) # 4³
print(result3) #64

#4. Max 
result4 = max(x, y, z)
print(result4) #5

#5. Min 
result5 = min(x, y, z)
print(result5) #3.14


#import math module at top

#6. constants
print(math.pi)
print(math.e)

#7. square root
result6 = math.sqrt(9)
print(result6) # 3.0

#8. Ceil - rounding up
result7 = math.ceil(88.84)
print(result7) # 89

#9. floor - rounding down
result8 = math.floor(88.62)
print(result8) # 88
