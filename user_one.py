# Module for User class ONLY.


class User(object):
    """A model for a user."""

    def __init__(self, first_name, last_name, age, country):
        """Intialize user info attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        """Simulate the user's information."""

        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Country: " + self.country.title())

    def greet_user(self):
        """Simulate a message to greet each user."""
        print("Greetings, " + self.first_name.title() + "!")
