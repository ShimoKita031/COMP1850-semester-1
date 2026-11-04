# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a person, given and validated values for name and date of birth.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if name == "":
            raise ValueError("Name must not be empty")
        if not isinstance(birth, date):
            raise TypeError("Day of birth must be in date format")

        self.name = name
        self.birth = birth

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    @staticmethod

    def initials(name):
        """
        Returns the initials of the name inputted.
        """
        initials = ""
        for i in name:
            if i.isupper() == True:
                initials = initials + i
        return initials

    def is_birthday(birth):
        """
        Returns if it is this person's birthday today.
        """
        today = date.today()
        if birth == today.strftime("%m-%d"):
            return True
        else:
            return False
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)