# this program asks a user to enter a name and stops when john is entered and prints all the wrong entris

name = input("Enter your name:").lower()
incorrect_names = []  # empty list containing all the incorrect names


# the loop below continues to ask for names until john is entered

while name != "john":
    incorrect_names += ({name})
    name = input("Enter your name:")

else:
    name == "john"

print(incorrect_names[0:])
