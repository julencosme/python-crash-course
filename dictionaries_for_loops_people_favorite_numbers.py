# Favorite Numbers: Print each person's name along with their favorite numbers.

favorite_numbers = {
        'Abe': ['6', '66', '6666'],
        'Boswell': ['4', '44', '4444'],
        'Francisco': ['7', '77', '7777'],
        'Jane': ['3', '33', '3333'],
        'Cecelia': ['0', '00', '0000'],
        }

for person, numbers in favorite_numbers.items():
    print("\n" + person.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + number)
        
