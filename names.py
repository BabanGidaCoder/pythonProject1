"""user enters the names of all pupils in a class, then type stop indicating all the names
have been entered then prints out all the names after"""

j = ""  # empty string counter
while True:
    pupil_names = input("Enter the names of all pupils: 'Type stop to finish")  # this asks for names until stop
    j += "1"       # adds the count to the empty string

    if pupil_names == 'stop':
        break
print(f"The total number of names is: {len(j)}")  # totals using len function then prints out the number

