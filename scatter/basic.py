import matplotlib.pyplot as plt

# Fixing random state for reproducibility

num = 4
x = range(num)
y = range(num)
z = range(num)

plt.scatter(x, y, c=z)
plt.show()
