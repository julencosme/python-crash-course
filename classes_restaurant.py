class Restaurant():
    """A model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize name and age attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Simulate a description of restaurant."""
        print(self.name.title() + " is the restaurant.")
        print(self.cuisine.title() + " is the type of cuisine.")

    def open_restaurant(self):
        """Simulate a message alerting that the restaurant is open."""
        print(self.name.title() + " is open.")


this_restaurant = Restaurant('diacos', 'micronesian')
this_restaurant.describe_restaurant()
this_restaurant.open_restaurant()
