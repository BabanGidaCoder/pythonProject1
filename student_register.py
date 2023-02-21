# this program asks the user to enter the amount of students to be registered and enters
# student ID in a text file

num_students = int(input("How many students are registering? "))    # input statement for the amount required

# file is open in write mode
with open("reg_form.txt", "w") as f:
    for i in range(num_students):
        student_id = input("Enter the student ID number: ")
        f.write(student_id + "\n")         # this write statement adds the ID numbers to the file

print("Done! The student ID numbers have been saved to reg_form.txt.")    # Finally output telling user Id nos have been saved
