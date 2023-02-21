# this program checks for leap years from the date entered and years requested

start_year = int(input("What year do you want to start with:"))  # takes input year from user
years = int(input("How many years do you want to check\n"))

for i in range(years):                  # loop checking the amount of years requested
    current_year = start_year + i       # adds 1 year to the start date entered
    if current_year % 4 == 0:
        print(f"{current_year} is a leap year")
    if current_year % 4 != 0:
        print(f"{current_year} is not a leap year")
#else:
    #print(f"{current_year} is not a leap year")
