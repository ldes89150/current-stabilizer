import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
import sys


# fname = sys.argv[1]
fname = 'new.csv'
data = mlab.csv2rec(fname, skiprows=2, names=['t', 'V'])

plt.plot(data["t"], data["V"],'-', label=r"$I_{set} = 150A$")
plt.xlabel(r"$t(seconds)$")
plt.ylabel(r"$V(Volts)$")

plt.show()