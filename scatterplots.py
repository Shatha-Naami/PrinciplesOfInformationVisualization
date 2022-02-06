import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 4, 5, 7, 8])
y = x
plt.figure()
plt.scatter(x, y)
plt.show()

# Example 2
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = x

# create a list of colors for each point to have
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red']
colors = ['green'] * (len(x) - 1)
colors.append('red')

plt.figure()

# plot the point with size 100 and chosen colors
plt.scatter(x, y, s=100, c=colors)
plt.show()

# Example 3

zip_generator = zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
x, y = zip(*zip_generator)
plt.figure()
plt.scatter(x[:3], y[:3], s=100, c='red', label='Tall students')
plt.scatter(x[3:], y[3:], s=100, c='blue', label='Short students')
plt.xlabel('The number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')
plt.legend(loc=4, frameon=False, title='Legend')
plt.show()
