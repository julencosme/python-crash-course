cities = {
    'provo': {
        'country': 'united states',
        'population': '117,335',
        'founded_incorporated': '1849',
    },
    'san francisco': {
        'country': 'united states',
        'population': '884,363',
        'founded_incorporated': '1850',
    },
    'arcata': {
        'country': 'united states',
        'population': '17,974',
        'founded_incorporated': '1858'
    }
}

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    founded_incorporated = city_info['founded_incorporated']
    print("\nCity: " + city.title())
    print("\nPopulation: " + population.title())
    print("\nFounded or incorporated: " + founded_incorporated.title())
