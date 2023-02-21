# this program reads data from text file DOB.txt and prints it out in 2 different sections


name_list = []
age_list = []
# variable to store the contents of the file
# opens the file for reading
f = open('DOB.txt', 'r')
# loop goes over each line in the file assigning name and age variables then add to name/age lists
for line in f:
    name, age = line.strip("\n").split(", ")

    name_list.append(name)
    age_list.append(age)
f.close()
for name in name_list:
    print(name)

for age in age_list:
    print(age)


# print(f"Name\n {name}")
# print(f"Age\n {age}")


# TODO seperate the names from the DOB and print in two different sections
