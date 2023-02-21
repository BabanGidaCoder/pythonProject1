# the code below inputs a sentence and displays each word on a separate line

inp_sen = input("Enter a sentence:")

inp_sen = inp_sen.split()  # used split function to separate the string

for word in inp_sen:       # the loop iterates the sentence and outputs the words on a new line

    print(word)



