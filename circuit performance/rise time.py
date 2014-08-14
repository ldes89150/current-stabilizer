import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
import sys


# fname = sys.argv[1]
fname = 'scope_0.csv'
data = mlab.csv2rec(fname, skiprows=2, names=['t', 'V'])



plt.plot(data["t"], data["V"], label=r"$I_{set} = 150A$")
plt.xlabel(r"$t(seconds)$")
plt.ylabel(r"$V(Volts)$")


# plt.show()
# You may want to preview the plot before determining parameters.

#===============================================================================
# parameters
#===============================================================================
start_time = -0.00296
end_time = 0.04

low_l_time = -0.03
low_r_time = -0.02

high_l_time = 0.02
high_r_time = 0.04

settle_err = 0.03

#------------------------------------------------------------------------------ 


i = 0
sum = 0.0
for d in data:
    if (d[0] > low_l_time) and (d[0] < low_r_time):
        i = i + 1
        sum = sum + d[1]
low_level = sum / i

i = 0
sum = 0.0
for d in data:
    if (d[0] > high_l_time) and (d[0] < high_r_time):
        i = i + 1
        sum = d[1] + sum
high_level = sum / i

ten_level = low_level + 0.1 * (high_level - low_level)
ninety_level = low_level + 0.9 * (high_level - low_level)


for d in data:
    if d[0] > start_time:
        if d[1] > ten_level:
            ten_pt = d
            break
for d in data:
    if d[0] > start_time:
        if d[1] > ninety_level:
            ninety_pt = d
            break

for d in data:
    if d[0] > start_time and d[0] < end_time:
        if np.abs(d[1] - high_level) > settle_err * (high_level - low_level):
            st_pt = d


x = np.ones(shape=len(data["t"]))

plt.plot(ten_pt[0], ten_pt[1] , "o")
plt.plot(data["t"], ten_pt[1] * x, "-.", label=r"$10 \%$")
plt.plot(ninety_pt[0], ninety_pt[1], "o")
plt.plot(data["t"], ninety_pt[1] * x, "-.", label=r"$90 \%$")
plt.plot(st_pt[0], st_pt[1], "o", label=r"$settle \, point(err \, in \," + str(100 * settle_err) + r"\% )$")


rise_time = ninety_pt[0] - ten_pt[0]
st_time = st_pt[0] - start_time

print "rise time =" , rise_time
print "{0}% settle time =".format(settle_err*100), st_time
title = "$rise \, time = {0}s, \; settle \, time = {1}s$".format(rise_time, st_time)
plt.title(r"" + title)
plt.legend()
plt.show()
