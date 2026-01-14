# default arguments 
# 
# argument types = 
#   1. positional 
#   2. default 
#   3. keyword 
#   4. arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1 + tax)

print(net_price(500, 0, 0.05)) # 525.0
print(net_price(500)) # 525.0
# when u skip one u use keyword for the other 
print(net_price(400, tax=0.2)) #480.0
