#----------------------------------------------------

# indexing - (indexing operator)
# accessing elements of a sequence using [start:end:step] 

# String indexing: allows you to access individual characters using positive (0-based) or negative (-1 from end) indices

# String slicing: uses [start:end:step] syntax to extract substrings, with start inclusive and end exclusive

# Negative indexing: provides convenient access to characters from the end of strings using negative numbers

# Step slicing: with [::step] enables advanced operations like reversing strings ([::-1]) and skipping characters

# Performance considerations: Slicing creates new string objects, so consider memory usage for large strings

# AI/ML applications: Essential for text preprocessing, tokenization, and data cleaning in machine learning pipelines

# Error handling: Python gracefully handles out-of-range indices without throwing errors, returning empty strings or partial results

#----------------------------------------------------

credit_number = '1234-5678-9012-3456'

print(credit_number[2]) # start (inclusive) 
#                       --> 3

print(credit_number[:8]) # end(exclusive) 
#                       --> 1234-567

print(credit_number[0:5]) #start(inclusive) - end(exclusive)
#                       --> 1234-

print(credit_number[5:]) # 5th position onwards
#                         --> 5678-9012-3456

print(credit_number[-1]) #last position 
#                         --> 6

#--------- STEP --------------

print(f"print every 3rd?{credit_number[::3]}")
#                 --> print every 3rd? 146-136
print(credit_number[0:4:2])
#                   --> 13

last_digits = credit_number[-4:] 
print(f"XXXX-XXXX-XXXX-{last_digits}") #XXXX-XXXX-XXXX-3456

#--------- REVERSE --------------
reverse_number = credit_number[::-1] 
print(reverse_number) # 6543-2109-8765-4321