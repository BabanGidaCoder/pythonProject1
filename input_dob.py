# this program reads data from text file DOB.txt and prints it out in 2 different sections

name = []
birthdate = []
# contents = ""
with open('DOB.txt', 'r+') as file:  # open the file for reading
    lines = file.readlines()
    for line in lines:
        words = line.split()

        name = words[0]

        birthdate = words[2]
        # contents += line
        # print(contents)
        print(" Name:" + name)
        print("Birthdate : " + birthdate)
