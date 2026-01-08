#tempreture converter

tempreture = float(input("Enter the tempreture: "))
unit = input("Enter the unit: celsius(C) or fahrenheit(F) : ")

if unit == "C":
    tempreture =  (tempreture * 9/5) + 32 
    print(f"The new tempreture is {round(tempreture)}°F.")
elif unit == "F":
    tempreture = (tempreture - 32) * 5/9
    print(f"The new tempreture is {round(tempreture)}°C.")
else:
    print(f"The unit you entered ({unit}) is invalid")        