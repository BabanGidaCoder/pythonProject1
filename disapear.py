# code below asks a user to input a string and which characters they would like to disappear
# and outputs the result

user_inp = input("Enter a string sentence:")
disappear = input("Which characters from above would you like to make disappear:")

# used the replace function to remove the requested characters

mod_string = user_inp.replace(disappear, "")
print(mod_string)
