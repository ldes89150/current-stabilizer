import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
import sys


# fname = sys.argv[1]
fname = 'long.csv'
data = mlab.csv2rec(fname, skiprows=2, names=['V'])
for i in range(len(data["V"])):
	data["V"][i] = data["V"][i]*(-1)
t = np.array([i for i in range(len(data["V"]))])
plt.title = "Long Term Measurement of B Field"
plt.plot(t, data["V"],'+', label="sampling rate = 1Hz")
plt.xlabel(r"$t(seconds)$")
plt.ylabel(r"$V(Volts)$")


plt.show()