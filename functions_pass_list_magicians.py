# Magicians: Make a list of magician's names.
# Pass the list to a function called show_magicians(), which prints the name
# of each magician in the list.


def show_magicians(names):
    """Print a list of magician names."""
    for name in names:
        msg = "Magician: " + name.title()
        print(msg)


magician_names = ['rockwell', 'wellrock', 'lockrow']
show_magicians(magician_names)
