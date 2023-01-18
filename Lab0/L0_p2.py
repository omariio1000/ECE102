import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 2*np.pi, 100)

x1 = 500 + 150.1 * np.cos(phi)
y1 = 500 + 150.1 * np.sin(phi)

x2 = 600 + 132.4 * np.cos(phi)
y2 = 500 + 132.4 * np.sin(phi)

x3 = 100 + 579 * np.cos(phi)
y3 = 700 + 579 * np.sin(phi)

fig, ax = plt.subplots()

ax.grid()
ax.plot(x1, y1, x2, y2, x3, y3)

A = np.arccos((132.4**2 - 150.1**2 - 100**2)/(-2 * 150.1 * 100))

it1 = 500 + 150.1 * np.cos(A)
it2 = 500 + 150.1 * np.sin(A)
it3 = 500 - 150.1 * np.sin(A)

print(f'({it1}, {it2})')
print(f'({it1}, {it3})')

ax.plot(it1, it2, marker='o', markersize=10, markerfacecolor='red')
ax.plot(it1, it3, marker='o', markersize=10, markerfacecolor='red')

plt.show()

