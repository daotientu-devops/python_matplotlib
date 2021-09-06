# Most of the matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
# The Pyplot package can be referred to as plt
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.5, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, startangle=90, explode=myexplode, colors=mycolors, shadow=True)
plt.legend(title="Four Fruits")
plt.show()