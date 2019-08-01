# Testing parameters for function: 'city_population.py'.

import unittest
from city_population import get_formatted_city_country


class CityCountryPopulationTestCase(unittest.TestCase):
    """Tests for city_functions,py' with added parameter for population."""

    def test_city_country_population(self):
        """Generate a test to verify city, country and population result in the correct string."""
        formatted_city_country_population = get_formatted_city_country(
            'Manila', 'Phillipines', 'population 13,698,889'
        )

        self.assertEqual(formatted_city_country_population,
                         'Manila, Phillipines: population 13,698,889')


unittest.main()
