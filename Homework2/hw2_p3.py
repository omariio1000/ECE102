import numpy as np
import matplotlib.pyplot as plt
import os

fileName = input("Enter file name: ")
#fileName = "reduced_data.txt"
if not(os.path.isfile(fileName)):
    print("ERROR: The file cannot be found.")
    quit()

#from here is just parsing data
rawText = np.genfromtxt(fileName)

vGSNum = int(rawText[0])
vDSNum = int(rawText[1])

idx = 2;
vGS = np.zeros(vGSNum)
for i in range(vGSNum):
    vGS[i] = float(rawText[idx])
    idx+=1

vDS = np.zeros(vDSNum)
for i in range(vDSNum):
    vDS[i] = float(rawText[idx])
    idx+=1



curr = np.zeros((vGSNum, vDSNum))
for i in range(vGSNum):
    for j in range(vDSNum):
        curr[i,j] = float(rawText[idx])
        idx+=1

# print(vGS)
# print(vDS)
# print(curr)

#this could be done in step above but got lazy and didn't want to change
adjCurr = np.zeros((vGSNum, vDSNum))
for i in range(vGSNum):
    for j in range(vDSNum):
        adjCurr[i,j] = curr[i,j] * vGS[i]

#everything below is for plotting
fig, ax = plt.subplots()

for i in range(vGSNum):
    ax.plot(vDS, adjCurr[i], label = f"V_GS = +{vGS[i]}") #, marker='o', markersize=4)

ax.grid()
ax.set_title(label='NMOS Characteristic Curves')
ax.set_xlabel('V_DS (V)')
ax.set_ylabel('I_D (mA)')
ax.legend()
plt.show()