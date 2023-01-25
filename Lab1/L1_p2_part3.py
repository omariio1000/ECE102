import numpy as np
import matplotlib.pyplot as plt

SampleECG = np.genfromtxt("badECG.txt")

time = np.linspace(0, 3, len(SampleECG))

avg = np.mean(SampleECG)
CorrectedECG = [-(sample - avg) for sample in SampleECG]

max = np.max(CorrectedECG)
amp = 10/max

CorrectedECG = [sample * amp for sample in CorrectedECG]

fig, ax = plt.subplots()
ax.plot(time, SampleECG, label='ECG Sample')
ax.plot(time, CorrectedECG, label='Corrected ECG Sample')

ax.grid()
ax.set_title(label='Sample ECG Data')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (mV)')
ax.legend()
plt.show()