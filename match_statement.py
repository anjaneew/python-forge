# Match-case statement (switch) 

# ----------Example ----------

#if-statement
def day_of_week(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    else:
        return "invalid"
    
print(f"Hello, have a great {day_of_week(1)}!")   
# Hello, have a great Monday!  

# Match case statement
def give_day(day):
    match day:
        case 1: 
            return "Monday"
        case 2:
            return "Tuesday"
        case _:
            return "invalid"


print(give_day(2))

#-----------Example 2 multiple cases-----------

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday")) # True
