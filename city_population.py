# Function that returns a single string in the form of:
# 'City, Country: population XXXXXXXX'.


def get_formatted_city_country(city, country, population=''):
    """Generate a neatly formatted city and country."""
    city_country = city.title() + ', ' + country.title() + ': ' + population
    return city_country


formatted_city_country_population = get_formatted_city_country(
    'arcata', 'united states', 'population 18,000')
print(formatted_city_country_population)
