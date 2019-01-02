# Making sure two lists are stored: a list with modified magician names and
# another list with unmodified magician names.


def make_great(magician_names):
    coll = []
    for magician_name in magician_names:
        coll.append(magician_name + " the Great")
    return coll


def show_magicians(magician_names):
    """Show the list of modified magician names."""
    for magician_name in magician_names:
        print(magician_name.title())


original_magician_names = ['rockwell', 'wellrock', 'lockrow']
print("\nThe following are unmodified magician names:")
show_magicians(original_magician_names)

modified_magician_names = make_great(original_magician_names)
print("\nThe following are modified magician names:")
show_magicians(modified_magician_names)
