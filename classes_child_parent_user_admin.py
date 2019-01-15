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


admin_a = Admin()
admin_a.describe_admin_privileges()
