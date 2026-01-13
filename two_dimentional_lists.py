fruits =     ["🍇","🍈","🍊","🍎","🍍"]
vegitables = ["🥔","🥕","🫑","🥒","🍆"]
meats =      ["🍗","🐟","🥩","🥓","🍖"]

groceries = [fruits, vegitables, meats]
# or we can add all in one list - same result 
# groceries = [["🍇","🍈","🍊","🍎","🍍"], 
#              ["🥔","🥕","🫑","🥒","🍆"]
#              ["🍗","🐟","🥩","🥓","🍖"]]

print(groceries) # all
print(groceries[0]) # ['🍇', '🍈', '🍊', '🍎', '🍍']
print(groceries[0][0]) # 🍇

#itirate over each item in nested loop
for type in groceries:
    for item in type:
        print(item, end="")
    print()    

'''
🍇🍈🍊🍎🍍
🥔🥕🫑🥒🍆
🍗🐟🥩🥓🍖
'''