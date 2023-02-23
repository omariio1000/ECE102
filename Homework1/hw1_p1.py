import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(0, 10, 100)
current = 5 * np.exp(-alpha)

fig, ax = plt.subplots()

ax.plot(alpha, current)
ax.set_title(label="\u03B1 vs i(\u03B1)")
ax.set_xlabel("\u03B1")
ax.set_ylabel("i(\u03B1)")
ax.axhline(y = 0.25, color = 'r', linestyle = 'dashed')
ax.grid()

plt.show()