# Most of the matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# The Pyplot package can be referred to as plt
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
# You can use the keyword argument marker to emphasize each point with a sepcified marker
plt.plot(ypoints, marker = '*')
plt.show()
# you can use also use the shortcut string notation parameter to specify the marker
# marker line color
plt.plot(ypoints, 'o--r')
plt.show()
# Marker size + color (mec: set the color of the edge of the marker)
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()
# mfc: set the color inside the edge of the marker
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# Use hexadecimal color value
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()