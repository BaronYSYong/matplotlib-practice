import numpy as np
import matplotlib.pyplot as plt

bins = 10
data = np.random.randn(1000, 3)

colors = ['blue','green', 'red']
plt.hist(data, bins, histtype='bar', color=colors, stacked=True, fill=True)

plt.show()
