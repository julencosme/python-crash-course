# Generating random motion of molecules; wrapping 'molecules_randomMotion.py'
# in a while loop to make sure the program continues to run.

import matplotlib.pyplot as plt

from motion_molecules import RandomMotion

# Keeping the motion going, as long as the program is active.
while True:
    # Making random motion, and plotting the points.
    rm = RandomMotion()
    rm.fill_motion()
    plt.plot(rm.x_values, rm.y_values, linewidth=.7)
    plt.show()

    keep_running = input("Continue motion of molecules? (y/n): ")
    if keep_running == 'n':
        break
