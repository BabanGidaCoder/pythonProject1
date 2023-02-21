"""Always asks the user to enter a number when -1 entered calculate the average excluding
the -1"""

total_num = 0
j = 0   # sets count to 0
# code below keeps asking for a number until -1 is entered
while True:
    user_number = int(input(" Enter a number"))
    j += 1
    total_num += user_number
    if user_number == -1:
        break

average = total_num / j

print(f"the average of the numbers entered is: {average}")



