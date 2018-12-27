# New attributes and methods pertaining to class: 'Restaurant', in order to increment the
# number of customers served in a day.


# Code from previous prompt: 'classes_methods_restuarant.py':
class Restaurant():
    """A model of a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize name and age attributes."""
        self.name = name
        self.cuisine = cuisine
        # Adding attribute 'number_served' with a default value of '0'.
        self.number_served = 0

    def describe_restaurant(self):
        """Simulate a description of restaurant."""
        print(self.name.title() + " is the restaurant.")
        print(self.cuisine.title() + " is the type of cuisine.")

    def open_restaurant(self):
        """Simulate a message alerting that the restaurant is open."""
        print(self.name.title() + " is open.")

    # def update_number_served(self, number_of_customers):
    def set_number_served(self, number_of_customers):
        """Set the number of customers served."""
        self.number_served = number_of_customers

    # def set_number_served(self):
    def print_number_served(self):
        """Print a statement displaying the number of customers served that day."""
        print("There were " + str(self.number_served) +
              " customers served today.")

    def increment_number_served(self, customers):
        """Add to the number of customers served in a given day."""
        self.number_served += customers


this_restaurant = Restaurant('diacos', 'micronesian')
this_restaurant.describe_restaurant()
this_restaurant.open_restaurant()

this_restaurant.set_number_served(78)
this_restaurant.print_number_served()

this_restaurant.increment_number_served(20)
this_restaurant.print_number_served()
