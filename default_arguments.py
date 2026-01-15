# default arguments 
# 
# argument types = 
#   1. positional  -usual way
#   2. default 
#   3. keyword 
#   4. arbitrary


# default arguments 
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1 + tax)

print(net_price(500, 0, 0.05)) # 525.0
print(net_price(500)) # 525.0

# keyword arguments 
# when u skip one u use keyword for the other 
# positional arguments first
print(net_price(400, tax=0.2)) #480.0


#example of a keyword argument in print
for x in range(1,11):
    print(x, end=" ") #end is a keyword argument
    # 1 2 3 4 5 6 7 8 9 10

print() 
#sep (seperator) is a keyword argument
print( 1, 2, 3, 4, 5, sep="***")   # 1***2***3***4***5 

#exercise  - my version
def create_phone_number(first_digits, last_digits, country_code="001", area_code="01"):
    print(country_code, area_code, first_digits, last_digits, sep="-")

create_phone_number("014", "125")    # 001-01-014-125

#exercise - tutor version
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}" # better than print cz its flexible

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num) #1-123-456-7890