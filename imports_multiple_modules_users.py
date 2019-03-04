# Importing methods from two modules ('user_one.py' & 'admin_privileges.py')
# concerning users and admin privileges.

from user_one import User
from admin_privileges import Privileges, Admin

user = User('brighton', 'banks', 34, 'kenya')
user.describe_user()
user.greet_user()

admin = Admin()
admin.describe_admin_privileges()
