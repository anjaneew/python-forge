# for loops --> useful when we have to do something for a limited number of times. 

#  for counter in range(begin, end)
for x in range(1, 11):
    print(x)

# reversed counting
for x in reversed(range(1,11)):
    print(f"{x} Happy new year")    


# steps counting
for x in reversed(range(1,11,2)):
    print(f"{x} Hi")      

# iterate over a string

credit_card = "1234-5678-1234-5678"

for x in credit_card:
    print(x)

# continue keyword - skip over iteration

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)    

# break keyword - break the loop

for x in range(1,21):
    if x == 9:
        break
    else:
        print(x) # only prints upto 8
