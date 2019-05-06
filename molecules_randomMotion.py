# Generating random motion of molecules, using the 'RandomMotion()' class.

import matplotlib.pyplot as plt

from motion_molecules import RandomMotion

# Creating random motion, and plotting the points.
rm = RandomMotion()
rm.fill_motion()

plt.plot(rm.x_values, rm.y_values, linewidth=.7)
plt.show()
# If saving the figure:
# plt.savefig('molecules_random_plot.png', bbox_inches='tight')
