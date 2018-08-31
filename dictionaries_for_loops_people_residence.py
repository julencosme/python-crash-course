# People: Make two new dictionaries representing different people, and store
# all three dicitonaries in a list called 'people'.
#
# Loop through your list of people. As you loop through the list, print
# everything you know about each person.

people = {
    'jwalton': {
        'first': 'joni',
        'last': 'walton',
        'age': '51',
        'residence': 'dallas',
    },
    'jpenn': {
        'first': 'julia',
        'last': 'penn',
        'age': '37',
        'residence': 'miami',
    },
    'oharper': {
        'first': 'oswald',
        'last': 'harper',
        'age': '70',
        'residence': 'detroit',
    },

}

for person, person_info in people.items():
    full_name = person_info['first'] + " " + person_info['last']
    age = person_info['age']
    residence = person_info['residence']
    print("\nPerson: " + person)
    print("\nFull name: " + full_name.title())
    print("\nAge: " + age)
    print("\nResidence: " + residence.title())
