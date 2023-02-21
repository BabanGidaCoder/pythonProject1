# An Email Simulation


class Email:
    """
     Has 4 variables below, has been read and is spam have been initialled to false
     The 2 immediately below are class variables set to false
     """
    has_been_read = False
    is_spam = False
    def __init__(self, sender_email_address, email_contents, from_address):
        """
        This is the constructors for the Email class including the sender email address.

        """
        self.sender_email_address = sender_email_address
        self.email_contents = email_contents
        self.from_address = from_address


    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True


email_1 = Email('jsge@gmail.com', False, 'test net', False, 'shede@hootmail.com')
email_2 = Email('jhge@gmail.com', False, 'test done', False, 'shade@hootmail.com')

inbox = [email_1, email_2

        ]


     def add_email(self, email_contents, from_address):
        new_email = Email(f"{email_contents}, + {from_address}")
        return new_email.title()



     def get_count(self):
        return f" The nos of messages is " + len(from_address)

def get_email(self):
        input_index = input("Enter index of email in inbox:")
        return get_email(input_index)
    inbox.mark_as_read()

def get_unread_emails(self):
    unread.list = []
    if has_been_read:
             unread.list = [inbox]
             return unread.list

def get_spam_email(self):
    spam.list = []
    if is_spam:
      spam.list = [Email]
    return spam.list


def __delitem__(self, i):
        del_email = input(" Enter email index to be deleted!:")
        inbox(del_email)


user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        read.get_email()

    elif user_choice == "mark spam":
         mark_spam.get_spam_email()

    elif user_choice == "send":
        send.add_email()

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
