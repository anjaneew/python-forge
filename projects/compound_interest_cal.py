# compound interest calculator

principal = 0.00
rate = 0
years = 0

while principal <= 0:
    principal = float(input("Enter the initial principal balance: $"))
    if principal <= 0: 
        print(f"The principal amount must be bigger than zero.")

while rate <= 0:
    rate = float(input("Enter the annual interest rate: "))
    if rate <= 0: 
        print(f"The annual interest rate must be bigger than zero.")

while years <= 0:
    years = int(input("Enter the time period in years: "))
    if years <= 0: 
        print(f"The time period in years must be bigger than zero.")        


final_amount = principal * pow((1 + (rate / 100)), years)

print(f"The final amount for ${principal:.2f} at {rate}% interest rate for the {years} years period is: ${final_amount:.2f}")