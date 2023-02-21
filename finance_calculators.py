import math

# This calculator allows users to use two different financial calculators for investments and
# home loan repayment calculations.

initial_choice = input('Choose either investment or bond from the menu below to proceed:').lower()

print("investment - to calculate the amount of interest you'll earn on your investment\n"
      "bond       - to calculate the amount you'll have to pay on a home loan")

# Interest_choice = 'simple' or 'compound'
simple = 'interest'
compound = 'interest'
# code below runs the investment calculator using conditionals for simple / compound interest


if initial_choice == 'investment':
    P = int(input("Enter the amount you are depositing:"))
    r = int(input("Enter the interest rate:"))
    t = int(input("Enter the number of years of investing:"))
    interest_choice = input("choose 'simple' or 'compound' interest:")
    if interest_choice == 'simple':
        si = (P * r * t) / 100
        a = P + si
        print("Final Amount:", a)
        print("Simple interest is:", si)
    elif interest_choice == 'compound':
        # a = P * math.pow((1 + r), t) #this formula produced large wrong figures
        a = P * ((
                             1 + r / 100) ** t)  # obtained this formula from https://www.analyticsvidhya.com/blog/2021/08/basic-financial-calculations-using-python/
        ci = a - P
        print("Final Amount:", a)
        print("Compound Interest:", ci)
# code block below calculates bond repayment.

elif initial_choice == 'bond':
    house_value = int(input("Enter the present value of the house:"))
    interest_rate = int(input("Enter the monthly interest rate:"))
    months_payback = int(input("Enter Number of months:"))
    pay_per_month = (interest_rate * house_value) / (1 - (1 + interest_rate) ^ (-months_payback))  # Corrected symbol ^ in formula
    pay_per_month = round(pay_per_month, 2)  # this rounds the answer to 2 decimal places
    print("Amount to repay each month:", pay_per_month)
else:
    print("You have not entered a valid input please enter a choice from options above!")
