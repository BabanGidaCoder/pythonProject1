# The code below was debugged using the stack trace to remove any bugs and logic to get the correct output below


def print_values_of(dictionary: dict, keys: list):   # defined the dictionary as dict and keys as a list
    for key in selected_list:                      # looping over selected list to print out values
        print(dictionary[key])                      # changed k to key


simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh!",
                         "maggie": " (Pacifier Suck)"}    # corrected ' with " to ensure homer as key value pair
selected_list = ["lisa", "bart", "homer"]              # created a list to display the correct values
print_values_of(simpson_catch_phrases, selected_list)  # call function to output selected list in the format below

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
