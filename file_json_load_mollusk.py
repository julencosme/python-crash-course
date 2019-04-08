# Reading the value stored in 'mollusk_name.json' and displaying a message to
# the user stating the mollusk type they are observing.

import json

filename = 'mollusk_name.json'
with open(filename) as f_obj:
    mollusk_name = json.load(f_obj)
    print("The mollusk you are currently observing is: " + mollusk_name + ".")
