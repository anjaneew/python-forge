# Python file detection

import os # os - operating system

# file_path = "file_handling/test.txt" # relative
file_path = "/home/anjaneew/python-forge/file_handling/test.txt"

'''
Relative = folder/test.txt
Absolute = C:/Users/BroCode/Desktop/test.txt

# dont't use (backslash) - (it is an escape)
either use (double backslash) or /(forward slash)
'''

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists. ☑️")

    if os.path.isfile(file_path):
        print("That is a file 💾.")
    elif os.path.isdir(file_path): 
        print("That is a directory 📁 (folder).")

else:
    print(f"That location doesn't exist.❌")    

