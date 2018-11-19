def make_car(manufacturer, model_name, **car_info):
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
