''' This program helps a small business to manage tasks assigned to each member of the team, whilst utilizing
two files a task file and user file to manage the login and details of the tasks assigned.
'''
from datetime import datetime

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# login section

username_list = []
password_list = []

user_data = open('user.txt', 'r')
      for line in user_data:
        ''' This loop strips the new line and splits the list into user and password lists then
        adds them to the username list and password list '''

        user, password = line.strip("\n").split(", ")
        username_list.append(user)
        password_list.append(password)

user_data.close()

# validate the login

username = input("Enter your username:\n")
while not username in username_list:
    print('You have entered an invalid Username please try again!')
    username = input("Enter your username:")

password_index = username_list.index(username)
password = input("Enter your password:\n")
while password != password_list[password_index]:
    password = input("Enter your password:")
print(f"Welcome {username}")

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input(''' Please Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r' and username == 'admin':
        # checking if the user logged in is admin and presenting additional menu for statistics #
        def reg_user(new_username, new_password):
            new_reg_user = f"{new_username}, {new_password}"
            return new_reg_user
    ''' 
    This function registers a user when 'r' is selected from the menu  
    '''
            #print("Welcome Admin you can see statistics and add a new user")

        # new_menu = input('select "Yes" to display total nos of Users and Tasks, "No" to continue:\n').lower()
        # if new_menu == "yes":
        #     nos_tasks = open('tasks.txt', 'r')
        #     for line in nos_tasks:
        #         assignee, title, description, due_date, date, completed = line.split(', ')
        #         print(f'Total nos of tasks is:' + str(len(title)))
        #         print(f'Total nos users registered:' + str(len(username_list)))
        # elif new_menu == "no":
        #     print('continue adding a new user below')

        new_username = input('Enter a new Username:')
        new_password = input('Enter a new password:')
        password_conf = input('Enter your new password again:')
        new_user = open('user.txt', 'a+')

        while new_password != password_conf:
            print("Your password has not matched please enter the correct password:")
            password_conf = input('Enter new password again')
        if new_password == password_conf:
            print("Registering a new user!\n")
            new_user.write(str(new_username) + ", " + str(new_password) + "\n")
            new_user.close()
    elif menu == 'r':
        print("Only admin can register users!")




    if menu == 'a':
        def add_task():

        tasks_open = open('tasks.txt', 'a+')

        task_username = input("\nEnter username of task assigned to:")
        task_title = input("\nEnter task title:")
        task_description = input("\nEnter a description of the task:")
        task_due_date = input("\n Enter the due date of the task:")
        current_date = datetime.now()
        if_complete = 'No'
        tasks_open.write(str(task_username) + ", " + str(task_title) + ", " + str(task_description)
                         + ", " + str(task_due_date) + ", " + str(current_date) + ", " + str(if_complete)
                         + "\n"
                         )
        tasks_open.close()
    add_task()


    elif menu == 'va':
       def view_all():
        tasks_open = open('tasks.txt', 'r')
        data = tasks_open.readlines()

        for pos, line in enumerate(data, 1):
            split_data = line.split(", ")
            output = f'________[{pos}]___________\n'
            output += f'Assigned to:\t\t\t{split_data[0]}\n'
            output += f'Task:\t\t\t\t{split_data[1]}\n'
            output += f'description:\t\t{split_data[2]}\n'
            output += f'Assigned date:\t\t{split_data[3]}\n'
            output += f'Due Date:\t\t\t{split_data[4]}\n'
            output += f'If Completed:\t\t{split_data[5]}\n'
            output += '______________________\n'
        print(output)
        tasks_open.close()
        view_all()

    if menu == 'vm':
        def view_mine():


    tasks_open = open('tasks.txt', 'r')
    username = input("Enter username:")

    for options in tasks_open:
        split_data = options.split(", ")
        if split_data[0] == username:  # check user logged in is user task assigned to #

            print(f'Assigned to:\t\t\t{split_data[0]}\n')
            print(f'Task:\t\t\t\t{split_data[1]}\n')

    tasks_open.close()
    view_mine()
    # elif username != split_data[0]:
    # print("Youre not logged in!")

    if menu == 'e':
        print('Goodbye!!!')

    exit()
    breakpoint()

else:
    print("You have made a wrong choice, Please Try again")
