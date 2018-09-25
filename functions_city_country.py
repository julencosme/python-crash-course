# City Names: Write a function called 'city_country()' that takes in the
# name of a city and its country.
#
# The function should return a string formatted like this: "Santiago, Chile".
#
# Call your function with at least three city-country pairs, and print the value
# that's returned.


def city_country(city_name, country_name):
    """Display a city and the country that it is in."""
    print(city_name.title() + ", " + country_name.title())


city_country(city_name='mexico city', country_name='mexico')
city_country(city_name='miami', country_name='united states')
city_country(city_name='berlin', country_name='germany')
