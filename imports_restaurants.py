# Importing methods from restaurant module.

from restaurant import Restaurant, IceCreamStand

# example data:
my_restaurant = Restaurant('qs', 'fast food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# example data:
my_stand = IceCreamStand('Pennys', 'ice cream shoppe')
my_stand.describe_restaurant()
my_stand.describe_ice_cream_flavors()
