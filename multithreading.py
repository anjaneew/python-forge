# multithreading = Used to perform multiple tasks concurrently 
#                  (multitasking) Good for I/O bound tasks like
#                                       (input output) 
#                  reading files or fetching data from APIs 
#                  threading.Thread(target=my_function)

import threading
import time

def walk_dog(name):
    time.sleep(8)
    print(f"{name} is Walking the dog🚶🦮.")

def take_out_trash(name1, name2):
    time.sleep(2)
    print(f"{name1} and {name2} are taking out the trash🗑️.")  

def get_mail():
    time.sleep(4)
    print("Getting the mail ✉️.")

# -------------One Thread----------
# # these functions are running on the same thread, 
# # that's why waiting in order
# walk_dog()
# take_out_trash()
# get_mail()

# -------------Multithreading - multitasking----------
# thread object
#        threading module > call constructor > pass in keyword argument
chore1 = threading.Thread(target=walk_dog, args=("Mark",)) 
#                                              tuple (note the ',' comma)

#start this thread
chore1.start()

chore2 = threading.Thread(target=take_out_trash, args=("Mark", "Rose"))
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# join method - makes us wait for threads to 
#               finish before rest of the program
chore1.join()
chore2.join()
chore3.join()
print("All done!")