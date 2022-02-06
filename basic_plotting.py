import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

mpl.get_backend()

# Way 1
plt.plot(2, 3, '*')
# plt.show()

# Way 2
# create a new figure
fig = Figure()

# associate fig with the backend
canvas = FigureCanvasAgg(fig)

# add a subplot to the fig
ax = fig.add_subplot(111)

# plot the point (3,2)
ax.plot(3, 2, '.')

# save the figure to test.png
canvas.print_png('test.png')

# Example 2
plt.figure()
# plot the point (3,2) using the circle marker
plt.plot(3, 2, 'o')
plt.plot(2, 3, '*')
# get the current axes
ax = plt.gca()
# Set axis properties [xmin, xmax, ymin, ymax]
ax.axis([0, 6, 0, 10])
plt.show()
