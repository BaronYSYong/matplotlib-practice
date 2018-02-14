import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Reference:
    https://stackoverflow.com/questions/37503735/plot-multiple-lines-on-subplots-with-pandas-df-plot
"""

fig, axes = plt.subplots(1, 3)

np.random.seed([3,1415])
df = pd.DataFrame(np.random.randn(100, 6), columns=list('ABCDEF'))
df = df.div(100).add(1.01).cumprod()
print df
df.iloc[:, :2].plot(ax=axes[0])
df.iloc[:, 2:4].plot(ax=axes[1])
df.iloc[:, 4:].plot(ax=axes[2])
plt.show()
