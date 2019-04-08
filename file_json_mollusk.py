# Program asking user for the mollusk type they are observing and using
# json.dump() to store it in a file.

import json

mollusk_name = input(
    "Please enter the type of mollusk you are currently observing: ")

filename = 'mollusk_name.json'
with open(filename, 'w') as f_obj:
    json.dump(mollusk_name, f_obj)
