import matplotlib.pyplot as plt
import numpy as np

plt.figure()
linear_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exponential_data = linear_data ** 2

xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3)
new_xvals = []

for item in xvals:
    new_xvals.append(item + 0.3)

plt.bar(new_xvals, exponential_data, width=0.3, color='red')
plt.show()
