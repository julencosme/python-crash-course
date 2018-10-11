# Great Magicians: Start with a copy of your program of magician names.
#
# Write a function called 'make_great()' that modifies the list of magicians
# by adding the phrase "the Great" to each magician's name.
#
# Call 'show_magicians()' to see that the list has actually been modified.


def make_great(original_magician_names, modified_magician_names):
    """Modifying an existing list of magician names to read "the Great" along with
    their names."""
    while original_magician_names:
        current_name = original_magician_names.pop()
        print("The Great " + current_name.title())
        modified_magician_names.append(current_name)


def show_magicians(modified_magician_names):
    """Show the list of modified magician names."""
    print("\nThe following magician names have been modified:")
    for modified_magician_name in modified_magician_names:
        print(modified_magician_name)


original_magician_names = ['rockwell', 'wellrock', 'lockrow']
modified_magician_names = []

make_great(original_magician_names, modified_magician_names)
show_magicians(modified_magician_names)
