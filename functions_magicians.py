# Functions concerning magicians.


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
