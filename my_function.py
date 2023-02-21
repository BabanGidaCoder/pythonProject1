# The program below defines my own functions and uses them as requested

def days_of_week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:
        print(day)


print(days_of_week())


# Code below takes in a sentence and replaces every second word with 'Hello'

def replace_hello(sentence):
    words = sentence.split()           # separate the sentence into words using split method
    for i in range(1, len(words), 2):  # starting at index 1 in the sentence then looping through every 2nd word
        words[i] = "Hello"
    return ' '.join(words)             # used the .join method to join the list back


sentence = "The quick brown fox jumped over the lazy dog"
print(replace_hello(sentence))
