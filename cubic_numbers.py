# Plotting first five cubic numbers.

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
plt.plot(input_values, cubes, linewidth=3)


plt.title("Cubic Numbers", fontsize=21)
plt.xlabel("Value", fontsize=13)
plt.ylabel("Cube of Value", fontsize=13)

plt.tick_params(axis='both', labelsize=13)

plt.savefig('cubes_plot.png', bbox_inches='tight')
