"""
This program asks for the name, age, hair colour and eye colour of a person and creates an adult class
then creates a subclass child with the same attributes as the adult however overrides the can drive method
to print out whether the person is old enough to drive or not
"""

name = input("Enter name:")
age = input("\nEnter age:")
eye_colour = input("\nEnter Eye Colour:")
hair_colour = input("\nEnter hair colour:")


class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        """ Initialise attributes of the class """

        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour


def can_drive(self):
    print(f"{name}" + "is old enough to Drive! ")


class Child(Adult):
    """ Initialise attributes of the parent class Adult  """

    def __init__(self, name, age, eye_colour, hair_colour):

        super().__init__(name, age, eye_colour, hair_colour)
        """ only attributes associated with child class"""

  def can_drive(self):
      self.age = 18
      if age >= 18:
       self.Adult()
       self.can_drive()
      else:
          var = self.age <= 18
          self.child()
          self.can_drive()
            

