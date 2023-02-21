
# ask user for number then prints out all the even numbers

user_input = int(input("Please enter a number:"))

j = 1

# use the while loop to iterate over the num

while j <= user_input:
    if j % 2 == 0:   # checking for even  numbers
        print(j)
    j += 1                    # goes to the next number in the loop

