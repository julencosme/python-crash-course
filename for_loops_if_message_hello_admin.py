user_names = ['Admin', 'Adam', 'Bob', 'Christina', 'Diane', 'Evan']

for user_name in user_names:
    if user_name == 'Admin':
        print("Greetings Admin, would you like to see a status report?")
    else:
        print("Greetings " + user_name + ", thank you for logging in.")
