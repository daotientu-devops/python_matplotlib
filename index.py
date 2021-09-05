# Most of the matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# The Pyplot package can be referred to as plt
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
# Add grid line to a plot using the grid() function
# Display only grid lines for the x-axis
# Set line properties for the grid
plt.grid(axis='y', color='green', linestyle='--', linewidth=5.5)
plt.show()
