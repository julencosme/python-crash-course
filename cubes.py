# Plotting first five cubed numbers

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
plt.plot(input_values, cubes, linewidth=3)


plt.title("Cubed Numbers", fontsize=21)
plt.xlabel("Value", fontsize=13)
plt.ylabel("Square of Value", fontsize=13)

plt.tick_params(axis='both', labelsize=13)

plt.savefig('cubes_plot.png', bbox_inches='tight')
