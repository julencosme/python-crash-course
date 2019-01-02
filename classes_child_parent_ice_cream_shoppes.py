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


# child class to Restaurant class; specifically, a subclass for ice cream shoppes:

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


ice_cream_shoppe_a = IceCreamStand('Igloo Ice Cream', 'dessert')
ice_cream_shoppe_a.describe_restaurant()
ice_cream_shoppe_a.describe_ice_cream_flavors()
