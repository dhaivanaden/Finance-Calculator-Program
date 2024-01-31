import math

# Print initial information
print("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")

# Allow for user to input choice
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If investment selected then allow for input of details, calculations, error warning and finally printing result
if user_choice == 'investment':
    deposit_amount = float(input("Enter amount of money you are depositing: "))
    interest_rate = float(input("Enter interest rate (as a percentage): "))
    years_investment = int(input("Enter number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    if interest_type == 'simple':
        interest = deposit_amount * (1 + (interest_rate / 100) * years_investment)
    elif interest_type == 'compound':
        interest = deposit_amount * math.pow((1 + interest_rate / 100), years_investment)
    else:
        print("Interest type invalid. Please enter either 'simple' or 'compound'.")
        exit()

    print(f"The amount you will get back after {years_investment} years at {interest_rate}% {interest_type} interest is: {round(interest, 2)}")

# If bond selected then allow for input of details, calculations and finally printing result
elif user_choice == 'bond':
    present_value = float(input("Enter present value of the house: "))
    interest_rate = float(input("Enter interest rate: "))
    months_repay = int(input("Enter number of months you plan to take to repay the bond: "))

    monthly_payment = (interest_rate / 100 / 12 * present_value) / (1 - math.pow(1 + interest_rate / 100 / 12, -months_repay))

    print(f"Monthly bond repayment will be: {round(monthly_payment, 2)}")

# If bond or investment is not selected then print error warning
else:
    print("Choice is invalid. Please enter either 'investment' or 'bond'.")