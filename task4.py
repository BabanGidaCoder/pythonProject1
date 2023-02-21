# Determine if integer is divisbile

num = int(input("Enter an integer:"))

if num % 2 == 0 and num % 5 == 0:
    print("Integer is divisible by 2 and 5")
elif num % 2 == 0 or num % 5 == 0:
    print(" Integer is divisible by 2 or 5")
else:
    num % 2 != 0 or num % 5 != 5
    print("Integer not divisible by 2 or 5")
