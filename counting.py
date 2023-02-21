

chars_counted = {'google.com'}

char_count = {}
for c in chars_counted:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1


string = "google.com"

print(chars_counted(string))
