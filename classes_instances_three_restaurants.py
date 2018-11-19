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


restaurant_a = Restaurant('Cafe Red', 'American breakfast')
restaurant_b = Restaurant('Cafe Blue', 'Spanish tapas')
restaurant_c = Restaurant('Cafe Green', 'Lebanese')

restaurant_a.describe_restaurant()
restaurant_b.describe_restaurant()
restaurant_c.describe_restaurant()
