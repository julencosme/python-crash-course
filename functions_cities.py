# Cities: Write a function called 'describe_city()' that accepts the name
# of a city and its country.
#
# The function should print a simple sentence, such as Reykjavik is in Iceland.
#
# Give the parameter for the counrty a defualt value.
#
# Call your function for three different cities, at least one of which is not in
# the default country.


def describe_city(name, country='Norway'):
    """Display information regarding a city's name and which country it is in."""
    print(name + " is in " + country + ".")


describe_city(name='Oslo')
describe_city(name='Bergen')
describe_city(name='Cordoba', country='Argentina')
