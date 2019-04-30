# Adding colormap to 'cubes.py' file and using a scatter plot graph rather than
# line plot graph.

import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Reds, edgecolor='none', s=40)

plt.title("Cubic Numbers", fontsize=21)
plt.xlabel("Value", fontsize=13)
plt.ylabel("Cube of Value", fontsize=13)

plt.tick_params(axis='both', labelsize=19)

plt.savefig('cubes_colorMap_plot.png', bbox_inches='tight')
