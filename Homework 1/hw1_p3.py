import numpy as np
import matplotlib.pyplot as plt

def sumPart(arr:np.ndarray, start:int, end:int):
    sum = 0
    for i in range(len(arr)):
        if (start <= i <= end):
            sum += arr[i]
    return sum

vDC = 9
r1 = 1000
r2 = 1200
r3 = 1500
r4 = 1800
r5 = 2200

r1 = r2 = r3 = r4 = r5 = 1000

rArr = np.array([r1, r2, r3, r4, r5])

sw = np.zeros(5)

for switch in range(len(sw)):
    if switch == 0: sw[switch] = 0
    else: sw[switch] = (sumPart(rArr, 1, switch) / sumPart(rArr, 0, switch)) * vDC

plt.bar(np.linspace(1, 5, 5), sw, width = 0.4)
plt.show()