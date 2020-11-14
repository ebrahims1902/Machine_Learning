#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot
from pandas import read_csv
import numpy as np
filename = "multi-linear.csv"
names = ['area','bedrooms','age','price']
data = read_csv(filename, names = names)
correlations = data.corr()
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,4,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()

