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


user_a = User('amber', 'atkins', 45, 'peru')
user_b = User('brighton', 'banks', 34, 'kenya')
user_c = User('calina', 'cortez', 56, 'india')

user_a.describe_user()
user_a.greet_user()

user_b.describe_user()
user_b.greet_user()

user_c.describe_user()
user_c.greet_user()
