# Most of the matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# The Pyplot package can be referred to as plt
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([2, 6])
ypoints = np.array([50, 250])
# Plotting x and y points
plt.plot(xpoints, ypoints)
plt.show()
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
# Plotting (Vẽ) without line
plt.plot(xpoints, ypoints, 'o')
plt.show()
# Multiple points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()
# Default X-Points
# If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, 4, 5 (etc. depending on the length of the y-points)
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()