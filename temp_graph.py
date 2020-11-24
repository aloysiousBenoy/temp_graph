#!/usr/bin/env python3
import subprocess as subp
import time
import matplotlib.pyplot as plt
import numpy as np

SAMPLES = 100
temps = []
count = 0
while count<SAMPLES:
    p = subp.run(["/usr/bin/vcgencmd","measure_temp"],universal_newlines=True,stdout=subp.PIPE)
    temp = p.stdout.split("=")[1].split("\'")[0]
    print("pass {}".format(count+1))
    temps.append(float(temp))
    count+=1
    time.sleep(1)
print("Temps collected : ")
print(temps)
np_temps = np.array(temps)
fig = plt.figure()
gs = fig.add_gridspec(1,1,hspace=0.3,wspace=0.15)
ax = fig.add_subplot(gs[0,0])
ax.set_title("cpu temp graph")
ax.plot(np.arange(SAMPLES),np_temps)
plt.savefig("samp.pdf",format="pdf")