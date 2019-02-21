# A module for class Restaurant

"""A set of classes that can be used to represent a restaurant."""


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


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""

    def __init__(self, name, cuisine):
        """Initialize attributes of parent class; then initialize attributes
         specific to an ice cream stand."""

        super().__init__(name, cuisine)
        flavors = "vanilla, chocolate, strawberry, and rocky road."
        self.flavors = flavors

    def describe_ice_cream_flavors(self):
        """Print a statement describing the ice cream flavors offered."""
        print("This ice cream stand has the following flavors: " + self.flavors)
