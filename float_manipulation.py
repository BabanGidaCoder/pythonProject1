#  This program asks the user to enter 10 float numbers and manipulates the numbers as requested
import math

user_string = input('Enter 10 floating numbers separated by space:')  # ask for user float input
user_list = user_string.split()                      # used split function to separate numbers

# loop below each item in list casting into float numbers
for i in range(len(user_list)):
    user_list[i] = float(user_list[i])

# used sum function to total numbers and output
total = sum(user_list)

print('Total of numbers is:', total)


maximum = max(user_list)
print('The Maximum Number is:', maximum)

minimum = min(user_list)
print('The minimum number is:', minimum)

average = sum(user_list) / len(user_list)
print('The average is :', round(average, 2))

# The median numbers

user_list.sort()
mid = user_list // 2
median = (user_list[mid] + user_list[~mid]) / 2
print('The median is:', median)
