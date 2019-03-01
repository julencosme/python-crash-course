# Using user module to call:'describe_user', 'greet_user' and 'describe_admin_privileges'.

from user import User, Privileges, Admin

user_a = User('amber', 'atkins', 45, 'peru')

user_a.describe_user()
user_a.greet_user()

admin_a = Admin()
admin_a.describe_admin_privileges()
