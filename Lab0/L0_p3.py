import numpy as np
import matplotlib.pyplot as plt

Sx = float(input("Enter the scaling factor Sx: "))
Sy = float(input("Enter the scaling factor Sy: "))
ThDeg = float(input("Enter the rotation angle (deg): "))

Th = np.radians(ThDeg)
#Th2 = np.radians(-ThDeg)

og = np.array([(0,0), (0,1), (1,0), (0,0)])
#print(og, '\n')

scale = np.array([(Sx, 0), (0, Sy)])
rot = np.array([(np.cos(Th), -np.sin(Th)), 
                (np.sin(Th), np.cos(Th))])

transform = np.matmul(rot, scale)
#transform = np.matmul(scale, rot)
print(transform, '\n')

new = np.matmul(transform, og.transpose()).transpose()
#new = np.matmul(og, transform)
#print(new, '\n')

print("\nAf = [%.4f, %.4f]" % (new[0][0], new[0][1]))
print("Bf = [%.4f, %.4f]" % (new[1][0], new[1][1]))
print("Cf = [%.4f, %.4f]" % (new[2][0], new[2][1]))

fig, ax = plt.subplots()
ax.plot(og[:,0], og[:,1])
ax.plot(new[:,0], new[:,1])
ax.grid()


plt.show()