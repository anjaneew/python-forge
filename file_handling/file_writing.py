# Python writing files (.txt, .json, .csv)
import json
import csv

text_data = "I am a fire rabbit 🐦‍🔥.\n"

file_path1 = "file_handling/output1.txt"  # relative or absolute

#-------------Version 1 mode "w"-----------------
# writing / creating / outputting/ overwriting
with open(file=file_path1, mode="w") as file:
    file.write(text_data)
    print(f"The text file '{file_path1} was created.")

'''
with statement 
 - used to wrap a block of code to execute
 - opens & closes file as well 
 - no need to close manually

open function - open(file_path1,"w")
 - returns a file object
 - 2 parameters (file path & mode)
 - modes : 
 w - write or overwriting
 x - will write if the file doesn't exists (if it exists FileExistsError)   
 a - append 
 r - read 

as keyword
 - when open function returns a file object ->
 - we use as keyword to give it a name 
 - just like instantiating a file object (like in constructor)
 - ex file = File()

.write() method
 -writes the file object with given data
 - ex: file.write(text_data)

confirmation message
 - print(f"text file '{file_path} was created.")
'''

#-------------Version 2 mode "x" FileExistsError:-----------------

file_path2 = "file_handling/output2.txt"  # relative or absolute

try:
    with open(file_path2, "x") as file:
        file.write(text_data)
        print(f"The text file '{file_path2} was created.")
except FileExistsError:
    print("That file already exists.")

# #-------------Version 3 mode "a" append:-----------------

try: 
    with open(file_path2, "a") as file:
        file.write(text_data)
        print(f"The text file '{file_path2}' was appended. ")
except FileExistsError:
    print("That file already exists.")     

#-----------Version 4 collections -> we need to iterate over:--------------

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path3 = "file_handling/output3.txt"

try:
    with open(file_path3, "w") as file:
        for employee in employees:
            file.write(employee + "\n") 
        print(f"The text file '{file_path3}' was written. ")
except FileExistsError:
    print("That file already exists.") 

#-----------Version 5 json -> json.dump(data, file, indent=4):------------  

'''
import json - at top
json.dump() -> creates a json string
'''

# json - a dictionary of key value pairs
employee_details = {
    "firstName" : "Joe",
    "lastName" : "Jackson",
    "gender" : "male",
    "age" : "28",
    "address" : {   
        "streetAddress" : "101",
        "city" : "San Diego",
        "state" : "CA"
    },
    "phoneNumbers" : [
        {"type" : "home", "number": "7349282382"}
    ]
}  

file_path4 = "file_handling/output4.json"

try:
    with open(file_path4, "w") as file:
        json.dump(employee_details, file, indent=4)
        print(f"The json file '{file_path4}' was written. ")
except FileExistsError:
     print("That file already exists.") 

#-----------Version 6 - csv -> writer -> iterate------------     

'''
csv - comma seperated values
import csv - at top
writer is an object that provides methods to write csv files
no new line - open(file_path5, "w", newline="")
'''

employees_details_list = [["Name", "Age", "Job"],
                          ["Spongebob", 30, "Cook"],
                          ["Patrick", 37, "Unemployed"],
                          ["Sandy", 27, "Scientist"]]

file_path5 = "file_handling/output5.csv"

try:
    with open(file_path5, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees_details_list:
            writer.writerow(row)
        print(f"The csv file '{file_path5}' was written. ")
except FileExistsError:
    print("That file already exists.")