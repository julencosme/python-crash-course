# Using 'random' module.
#
# Creating class 'Dice', with a method 'roll_die', that rolls a die with a specified
# number of sides and a specified number of rolls of that particular die.
#
# As an example: using a six-sided die, ten-sided die, and twenty-sided die; rolling each die
# ten times.

from random import randint


class Dice():
    """An attempt to represent a die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, number_of_rolls=1):
        for sides_of_die in range(0, number_of_rolls):
            print(randint(1, int(self.sides)))


die = Dice()
die.roll_die(10)

die = Dice(10)
die.roll_die(10)

die = Dice(20)
die.roll_die(10)
