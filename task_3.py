# display count down from 20 to 0 using while loop

x = 20
while x >= 0:
    print(x)
    x -= 1  # decreases by 1 each time loop runs

# display even numbers from 1 to 20

for i in range(1, 20):  # iterates from 1 to 20 then checks for even numbers using % operator
    if i % 2 == 0:
        print(i)

# loop to display * on several lines

for i in range(0, 6):

    print('*' * i)

