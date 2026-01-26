# Python reading files (.txt, .json, .csv)
import json
import csv

file_path1 = "file_handling/output1.txt"
file_path2 = "file_handling/output2.txt"
file_path3 = "file_handling/output3.txt"
file_path4 = "file_handling/output4.json"
file_path5 = "file_handling/output5.csv"

# # --------------- Version 1 text---------------
# try:
#     with open(file_path1, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("File access was denied.")   

# # --------------- Version 2 json---------------
# # import json - at top

# try:
#     with open(file_path4, "r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("File access was denied.") 

# # ------- Version 3 json - using specific key -------
# # import json - at top

# try:
#     with open(file_path4, "r") as file:
#         content = json.load(file)
#         print(content["phoneNumbers"]) # [{'type': 'home', 'number': '7349282382'}]
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("File access was denied.")    

# --------------- Version 4 csv---------------     
# import csv - at top

try:
    with open(file_path5, "r") as file:
        content = csv.reader(file)
        # print(content) # <_csv.reader object at 0x72f711217300>
        for line in content:
            print(line)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("File access was denied.") 

# --------------- Version 5 csv by index---------------     
# import csv - at top

try:
    with open(file_path5, "r") as file:
        content = csv.reader(file)
        # print(content) # <_csv.reader object at 0x72f711217300>
        for line in content:
            print(line[0]) # (first column)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("File access was denied.")     