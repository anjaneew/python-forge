# Python writing files (.txt, .json, .csv)

text_data = "I am a fire rabbit 🐦‍🔥."

file_path = "file_handling/output.txt" 

# writing / creating / outputting
with open(file=file_path, mode="w") as file:
    file.write(text_data)
    print(f"text file '{file_path} was created.")

'''
with statement 
 - used to wrap a block of code to execute
 - opens & closes file as well 
 - no need to close manually

open function
 - returns a file object
 - 2 parameters (file path & mode)
 - modes : 
 w - write 
 x - will write if the file already exists (if not FileExistsError)   
 a - append 
 r - read 

as keyword
 - when open function returns a file object ->
 - we use as keyword to give it a name 
 - just like instantiating a file object (like in constructor)
 - ex file = File()
'''


