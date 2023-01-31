import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x = np.arange(-3, 3.1, 0.1)
y = np.arange(-3, 3.1, 0.1)

X, Y = np.meshgrid(x, y)
z = (np.sin(X*Y))**2

fig, ax = plt.subplots()

for i in range(len(x)):
    for j in range(len(y)):
        c = ""

        if (z[i][j] < 0.1): c = "b"
        elif (z[i][j] < 0.5): c = "c"
        elif (z[i][j] < 0.75): c = "g"
        elif (z[i][j] < 0.95): c = "r"
        else: c = "k"

        ax.plot(x[i], y[j], marker='s', color=c)

ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()