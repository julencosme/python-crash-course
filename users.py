# Module for classes: 'User', 'Privileges', 'Admin'.


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


class Privileges():
    """Represent admin user's privileges."""

    def __init__(self):
        self.privileges = ["can add a post", "can delete a post",
                           "can ban a user", "can add admin user"]

    def describe_admin_privileges(self):
        print("Privileges of the admin user(s) are as follows: " +
              str(self.privileges))


class Admin(Privileges):
    """Represent the privileges, specific to an admin user."""

    def __init__(self):
        """Intialize the attributes of the parent class."""
        super().__init__()
