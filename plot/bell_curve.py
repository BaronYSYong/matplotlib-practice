import matplotlib.pyplot as plt
import math

x = range(0,180,2)
y = []
for i in x:
    y.append((math.sin(math.radians(i) - 0.25)+1)/2)

plt.plot(x,y,'g')
plt.show()
