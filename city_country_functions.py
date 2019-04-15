# Creating a module called 'city_country_functions.py'
# This module will print out a string of the name of a city and the name of a country.


def get_formatted_city_country(city, country):
    """Generate a neatly formatted city and country."""
    city_country = city + ' ' + country
    return city_country.title()
