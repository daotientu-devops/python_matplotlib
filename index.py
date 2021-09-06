# Most of the matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# The Pyplot package can be referred to as plt
import matplotlib.pyplot as plt
import numpy as np
# this will generate a random result
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()