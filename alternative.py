# this code below reads a string and makes each alternate character an uppercase and each other alternate character
# a lowercase

alt_case = ""  # defining empty variable to store the output of the modified string
string = "Hello World"
# using a for loop to iterate each character in the string then checking for even/odd nos then
# convert to upper/lower the print the result

for i, c in enumerate(string):
    if i % 2 == 0:
        alt_case += c.upper()
    else:
        alt_case += c.lower()

print(alt_case)

# The following code uses the same string but makes each alternative word lower and upper case

alt_word = ""       # empty variable to hold the output
string = "hello world"

alt_word = string.split()         # used the split and join functions slicing the string into upper/lower case words
alt_word = string[0:5].upper(), string[6:11].lower()
alt_word = " ".join(alt_word)

print(alt_word)
