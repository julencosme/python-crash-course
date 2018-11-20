# Styling functions with proper indentation:


# Program for 'make_shirt' function:
def make_shirt(size, message):
    """Display information regarding the size and message of a shirt."""
    print("The shirt size is " + size +
          " and the message will read: " + message + ".")


make_shirt('large', 'Archaeology Club')


def make_shirt(size, message):
    """Display information regarding the size and message of a shirt."""
    print("The shirt size is " + size +
          " and the message will read: " + message + ".")


make_shirt(size='large', message='Archaeology Club')


# Program for 'make_car' function:
def make_car(
        manufacturer, model_name, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model_name
    for key, value in car_info.items():
        car[key] = value
    return car


car_profile = make_car(
    'mercedes', '240D', color='silver',
    tow_package=False)

print(car_profile)
