import numpy as np
import matplotlib.pyplot as plt

SampleECG = np.genfromtxt("SampleECGdata.txt")

min = np.min(SampleECG)
max = np.max(SampleECG)
avg = np.mean(SampleECG)

time = np.linspace(0, 1, 256)
time2 = time[0:257:2]
time10 = time[0:257:10]

ssRate = int(input("Enter desired subsample rate: "))
sub =  SampleECG[0:257:ssRate]
ss2 = SampleECG[0:257:2]
ss10 = SampleECG[0:257:10]
print(f"The length of the subsampled ECG is {len(sub)}.")

print(f"MIN = {min:.3f}, MAX: {max:.1f}, and the MEAN is {avg:.5e}")

CorrectedECG = [sample - avg for sample in SampleECG]

newAvg = np.mean(CorrectedECG)
print("The new mean is:", newAvg)

fig, ax = plt.subplots()
ax.plot(time, SampleECG, label='ECG Sample')
ax.plot(time, CorrectedECG, label='Corrected ECG Sample')
ax.plot(time2, ss2, label='Subsampled ECG Sample (n=2)')
ax.plot(time10, ss10, label='Subsampled ECG Sample (n=10)')
ax.grid()
ax.set_title(label='Sample ECG Data')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (mV)')
ax.legend()

plt.show()