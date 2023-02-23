import numpy as np
import matplotlib.pyplot as plt

def sumPart(arr:np.ndarray, start:int, end:int):
    sum = 0
    for i in range(len(arr)):
        if (start <= i <= end):
            sum += arr[i]
    return sum

vDC = 9
r1 = 6800
r2 = 1800
r3 = 3300
r4 = 6800
r5 = 10000

rArr = np.array([r1, r2, r3, r4, r5])

sw = np.zeros(5)

for switch in range(len(sw)):
    if switch == 0: sw[switch] = 0
    else: sw[switch] = (sumPart(rArr, 1, switch) / sumPart(rArr, 0, switch)) * vDC
    print(f"Switch {switch} pressed: {sw[switch]:.2f} V")

gaps = np.zeros(5)
for i in range(len(gaps)):
    if (i != len(gaps) - 1): gaps[i] = sw[i + 1] - sw[i]
    else: gaps[i] = vDC - sw[i]

labels = ["1 & 2 gap","2 & 3 gap", "3 & 4 gap", "4 & 5 gap", "5 and No gap"]

plt.bar(labels, gaps)
plt.xlabel("Switch Gaps")
plt.ylabel("Voltage Gap (V)")
plt.title("Voltage Gaps")
plt.show()