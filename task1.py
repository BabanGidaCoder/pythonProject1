num1 = int(2)
num2 = int(3)
num3 = int(4)

# compares num1 and num2 and display the larger number

if num1 > num2:
    print(f"{num1}")
else:
    num2 > num1
    print(f"{num2}")

    # determine if num1 is odd or even

    if num1 % 2 == 0:
        print(f" {num1} is even")
    else:
        print(f"{num1} is odd")

    # this checks for the largest number

    if num1 > num2 and num3:
        print(f"{num1}")
    elif num2 > num3 and num1:
        print(f"{num2}")
    elif num3 > num2 and num1:
        print(f"{num3}")

    # this checks for the second largest number

    if num1 > num2:
        print(f"{num1}")
    elif num2 > num1:
        print(f"{num2}")
if num3 > num1:
    print(f"{num1}")

# num3 > num1 or num2
# print(f"{num3}")
