#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:22:37 2023

@author: romainwlodarczyk
"""

from scipy.io import loadmat
import matplotlib.pyplot as plt

mat = loadmat("L2_PL1.mat")
#mat = loadmat("L2_PL2.mat")
#mat = loadmat("L2_PL3.mat")
#mat = loadmat("L2_PL4.mat")

psal = mat['psal_int']
ptemp = mat['ptemp_int']
pres = mat['p_int']

#plt.plot(ptemp, pres)
plt.pcolor(psal)
plt.colorbar()









