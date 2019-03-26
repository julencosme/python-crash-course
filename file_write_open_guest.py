guest = input("Please enter your first and last name: ")
filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(guest)
