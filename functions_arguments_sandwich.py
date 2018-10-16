# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the
# function call provides, and it should print a summary of the sandwich that
# is being ordered.
#
# Call the function three times, using a different number of arguments each
# time.


def make_sandwich(*fixings):
    """Print the list of fixings that have been requested for a sandwich."""
    print(fixings)


make_sandwich('ham', 'mustard')
make_sandwich('tofu', 'cilantro', 'cucumber', 'hoisin sauce')
make_sandwich('lox', 'capers', 'cream cheese')
