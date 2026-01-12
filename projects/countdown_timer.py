import time

# #my version2: 
# for x in reversed(range(1,11)):
#     if x == 1:
#         time.sleep(1)
#         print(x)
#         time.sleep(1)
#         print("Happy new year!!!") 
#         break  
#     else: 
#         time.sleep(1)
#         print(x)


# #my version1: 
# for x in reversed(range(1,11)):
#     print(x)

# print("Happy new year!!!")    

my_time = int(input("Enter time: "))

#or reverse
for x in range(my_time, 0, -1 ):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours =  int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")    