"""
Compulsory Task 1: 
------------------

Copy the code provided below to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""


def course_location():
    print("location:" + "Cape Town")


def show_course_id():
    print(" Course ID:" + "12345")


class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def __init__(self, description, trainer):
        self.description = description
        self.trainer = trainer

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def trainer_details(self):
        print(f"This course is about {self.description} thought by {self.trainer} ")


class OOPCourse(Course):
    """
    Subclass of course inheriting description and trainer
    """
    def __init__(self, description, trainer: object):

        super().__init__(description, trainer)

    def description(self):
        self.description = "OOP Fundamentals"

    def trainer(self):
        self.trainer = "Mr Anon A Mouse"


course_1 = Course('OOP Fundamentals', 'Mr Anon A Mouse')

course_location()
course_1.contact_details()
course_1.trainer_details()
show_course_id()
