# Adding a function that increments the number of user login attempts to the
# User class.
# Adding another function that resets the value of login attempts to zero to the
# User class.


class User(object):
    """A model for a user."""

    def __init__(self, first_name, last_name, age, country):
        """Intialize user info attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        """Simulate the user's information."""

        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Country: " + self.country.title())

    def greet_user(self):
        """Simulate a message to greet each user."""
        print("Greetings, " + self.first_name.title() + "!")

    def update_login_attempts(self):
        """Set the login attempts to the given value.
        Then, rejecting the change if it attepmts to roll back the login attempts.
        """
        if self.login_attempts >= self.login_attempts:
            self.login_attempts = self.login_attempts
        else:
            print("You cannot have a negative amount of login attempts.")

    def increment_login_attempts(self, number_of_logins):
        """Add the given amount to the login attempts reading."""
        self.login_attempts += number_of_logins
        print("There have been " +
              str(self.login_attempts) + " attempt(s) to login.")

    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0
        print("There have been " + str(self.login_attempts) + " attempts to login.")


user_a = User('amber', 'atkins', 45, 'peru')
user_b = User('brighton', 'banks', 34, 'kenya')
user_c = User('calina', 'cortez', 56, 'india')

user_a.describe_user()
user_a.greet_user()
user_a.update_login_attempts()
user_a.increment_login_attempts(1)
user_a.reset_login_attempts()
user_a.increment_login_attempts(100)
user_a.reset_login_attempts()


user_b.describe_user()
user_b.greet_user()
user_b.update_login_attempts()
user_b.increment_login_attempts(2)
user_b.reset_login_attempts()
user_b.increment_login_attempts(200)
user_b.reset_login_attempts()


user_c.describe_user()
user_c.greet_user()
user_c.update_login_attempts()
user_c.increment_login_attempts(3)
user_c.reset_login_attempts()
user_c.increment_login_attempts(300)
user_c.reset_login_attempts()
