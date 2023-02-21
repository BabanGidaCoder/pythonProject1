# this program asks user for a number then prints out the times table to 12 places

num = int(input("Enter a number:"))    # ask for number as an integer
print(f"The {num} times table is:")

for y in range(1, 13):                 # loop for 1 -12

    print(f"{num} * {y} = {num * y}")   # Multiplication table output

