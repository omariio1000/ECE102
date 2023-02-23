import numpy as np

mat = np.matrix([(11, -8, 0), (-8, 14, -2), (0, -2, 9)])
vec = np.array([(12), (0), (5)])

mesh = np.linalg.solve(mat, vec)

print(f"I\u2081: {mesh[0]:.2f}A")
print(f"I\u2082: {mesh[1]:.2f}A")
print(f"I\u2083: {mesh[2]:.2f}A")

i1 = mesh[0]
i2 = mesh[0] - mesh[1]
i3 = -mesh[1]
i4 = mesh[1] - mesh[2]
i5 = -mesh[2]

print(f"\nR\u2081: {i1:.2f}\u2126")
print(f"R\u2082: {i2:.2f}\u2126")
print(f"R\u2083: {i3:.2f}\u2126")
print(f"R\u2084: {i4:.2f}\u2126")
print(f"R\u2085: {i5:.2f}\u2126")

print(f"\nThe power dissipated by R\u2082 is {(i2 ** 2) * 8:.2f}W")