# Adding method, 'upgrade_battery()' to class 'Battery()'.


class Car():
    """An attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odomter_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    """An attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize battery attributes."""
        self.battery_size = battery_size
        self.range = 0

    def describe_battery(self):
        """Print a statement describing battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery_size(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("You have upgraded your battery size to " +
                  str(self.battery_size) + "-kWh.")
        else:
            print("You have the upgraded size of 85 already.")

    def get_range(self):
        """Print statement concerning the range this battery provides."""
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270

        message = "This car can go approximately " + str(self.range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represent aspects of an electric vehicle."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery_size()

my_tesla.battery.get_range()
