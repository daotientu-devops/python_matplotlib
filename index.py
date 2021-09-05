# Most of the matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# The Pyplot package can be referred to as plt
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
# Use the keyword argument linestyle or ls to change the style of the plotted line
plt.plot(ypoints, linestyle='dotted')
plt.show()
plt.plot(ypoints, linestyle='dashed')
plt.show()
plt.plot(ypoints, ls=':')
plt.plot(ypoints, color='r')
plt.show()
plt.plot(ypoints, c='#4CAF50', linewidth='20.5')
plt.show()
# Multiple lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()
# Plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()