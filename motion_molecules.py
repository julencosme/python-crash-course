# Creating a class that generates random motion.

from random import choice


class RandomMotion():
    """A class to generate random motion."""

    def __init__(self, num_points=5000):
        """Initialize attributes of motion."""
        self.num_points = num_points

        # All motion starts at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_motion(self):
        """Calculate all points of the motion."""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_movement = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_movement = y_direction * y_distance

            # Rejecting motion that goes nowhere.
            if x_movement == 0 and y_movement == 0:
                continue

            # Calculating the next x and y values.
            next_x = self.x_values[-1] + x_movement
            next_y = self.y_values[-1] + y_movement

            self.x_values.append(next_x)
            self.y_values.append(next_y)
