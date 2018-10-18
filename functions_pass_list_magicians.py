def show_magicians(names):
    """Print a list of magician names."""
    for name in names:
        msg = "Magician: " + name.title()
        print(msg)


magician_names = ['rockwell', 'wellrock', 'lockrow']
show_magicians(magician_names)
