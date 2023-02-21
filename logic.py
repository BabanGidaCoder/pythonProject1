# This code below demonstrates logic errors

i = 12               # since we start iterating from 12 the program would run with no output
for i in range(1, 10):
    if i > 10:          # logic is off as we defined 12 as in above 
        print(i)

