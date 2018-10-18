def describe_city(name, country='Norway'):
    """Display information regarding a city's name and which country it is in."""
    print(name + " is in " + country + ".")


describe_city(name='Oslo')
describe_city(name='Bergen')
describe_city(name='Cordoba', country='Argentina')
