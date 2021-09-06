# Most of the matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# The Pyplot package can be referred to as plt
import matplotlib.pyplot as plt
import numpy as np
# subplot() function to draw multiple plots in one figure
# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
# the figure has 1 row, 2 columns and this plot is the first plot
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("SALES")
# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
# the figure has 1 row, 2 columns and this plot is the second plot
plt.subplot(2, 3, 2)
plt.plot(x, y)
plt.title("INCOME")
# plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
# the figure has 1 row, 2 columns and this plot is the 3 plot
plt.subplot(2, 3, 3)
plt.plot(x, y)
# plot 4:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
# the figure has 1 row, 2 columns and this plot is the 4 plot
plt.subplot(2, 3, 4)
plt.plot(x, y)
# plot 5:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
# the figure has 1 row, 2 columns and this plot is the 4 plot
plt.subplot(2, 3, 5)
plt.plot(x, y)
# plot 6:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
# the figure has 1 row, 2 columns and this plot is the 4 plot
plt.subplot(2, 3, 6)
plt.plot(x, y)
# Super title
plt.suptitle("MY SHOP")
plt.show()
