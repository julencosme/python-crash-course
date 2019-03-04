# Using user module to call:'describe_user', 'greet_user' and 'describe_admin_privileges'.

from user import User, Privileges, Admin

user = User('amber', 'atkins', 45, 'peru')

user.describe_user()
user.greet_user()

admin = Admin()
admin.describe_admin_privileges()
