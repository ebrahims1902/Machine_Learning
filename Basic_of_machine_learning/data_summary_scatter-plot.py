#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:18:15 2020

@author: ebrahim
"""


from matplotlib import pyplot
from pandas import read_csv 
from pandas.plotting import scatter_matrix
filename = 'multi-linear.csv'
names = ['area','bedrooms','age','price']
data = read_csv(filename, names = names)
scatter_matrix(data)

pyplot.show()