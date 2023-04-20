#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 08:10:24 2023

@author: g22001430
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

f = open('PHYBIO2023_CHIMIE.csv')
data = np.genfromtxt(f,delimiter=';', missing_values='NA',skip_header=1)

PROF = data[0:,7]
TMP = data[0:,8]
SAL = data[0:,9]
OXY = data[0:,10]
OXYV = data[0:,11]
NO3NO2 = data[0:,14]
NO3NO2_f = data[0:,15]
PO4 = data[0:,17]
PO4_f = data[0:,18]
ALU = data[0:,20]
ALU_f = data[0:,21]
del(data)

# SUPPRESSION DES VALEURS MANQUANTES 
df1 = pd.DataFrame({'prof': PROF, 'nitrates': NO3NO2})
df1 = df1.dropna()
prof_N = df1['prof']
N = df1['nitrates']

df2 = pd.DataFrame({'prof': PROF, 'phosphates': PO4})
df2 = df2.dropna()
prof_P = df2['prof']
P = df2['phosphates']

df3 = pd.DataFrame({'prof': PROF, 'aluminium': ALU})
df3 = df3.dropna()
prof_A = df3['prof']
A = df3['aluminium']


# PROFILS ALU 
labels_surf = ['ST K - 07/03', 'ST K2 - 07/03']
plt.figure()              
plt.plot(A[0:11], -prof_A[0:11], '-o', linewidth=1)
plt.plot(A[11:22], -prof_A[11:22], '-o', linewidth=1)
plt.xlabel('Al (nmol/kg)', fontsize=9)
# plt.gca().xaxis.set_tick_params(labelsize = 7)
plt.ylabel('PROF (m)', fontsize=9)
# plt.gca().yaxis.set_tick_params(labelsize = 7)
plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.set_ticks_position('top')
plt.legend(labels_surf)
plt.title('Profils des concentrations en aluminium')

# PROFILS NITRATES TOUTES ST
labels_prof = ['ST D - 06/03','ST D3 - 06/03','ST K - 07/03','ST K2 - 07/03','ST B - 07/03','ST D - 08/03','ST D5 - 08/03','ST D3 - 08/03']
plt.figure()    
plt.plot(N[0:3], -prof_N[0:3], '-o', linewidth=1)          
plt.plot(N[3:14], -prof_N[3:14], '-o', linewidth=1)
plt.plot(N[14:25], -prof_N[14:25], '-o', linewidth=1)
plt.plot(N[25:35], -prof_N[25:35], '-o', linewidth=1)
plt.plot(N[35:41], -prof_N[35:41], '-o', linewidth=1)
plt.plot(N[41:45], -prof_N[41:45], '-o', linewidth=1)
plt.plot(N[45:56], -prof_N[45:56], '-o', linewidth=1)
plt.plot(N[56:66], -prof_N[56:66], '-o', linewidth=1)
plt.xlabel('NO3NO2 (µmol/kg)', fontsize=9)
# plt.gca().xaxis.set_tick_params(labelsize = 7)
plt.ylabel('PROF (m)', fontsize=9)
# plt.gca().yaxis.set_tick_params(labelsize = 7)
plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.set_ticks_position('top')
plt.legend(labels_prof)
plt.title('Profils des concentrations en nitrates - toutes stations')

# PROFILS PHOSPHATES TOUTES ST 
labels_prof = ['ST D - 06/03','ST D3 - 06/03','ST K - 07/03','ST K2 - 07/03','ST B - 07/03','ST D - 08/03','ST D5 - 08/03','ST D3 - 08/03']
plt.figure()    
plt.plot(P[0:3], -prof_P[0:3], '-o', linewidth=1)          
plt.plot(P[3:14], -prof_P[3:14], '-o', linewidth=1)
plt.plot(P[14:25], -prof_P[14:25], '-o', linewidth=1)
plt.plot(P[25:36], -prof_P[25:36], '-o', linewidth=1)
plt.plot(P[36:42], -prof_P[36:42], '-o', linewidth=1)
plt.plot(P[42:50], -prof_P[42:50], '-o', linewidth=1)
plt.plot(P[50:61], -prof_P[50:61], '-o', linewidth=1)
plt.plot(P[61:71], -prof_P[61:71], '-o', linewidth=1)
plt.xlabel('PO4 (µmol/kg)', fontsize=9)
# plt.gca().xaxis.set_tick_params(labelsize = 7)
plt.ylabel('PROF (m)', fontsize=9)
# plt.gca().yaxis.set_tick_params(labelsize = 7)
plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.set_ticks_position('top')
plt.legend(labels_prof)
plt.title('Profils des concentrations en phosphates - toutes stations')

# COMPARAISON NITRATES PHOSPHATES ST K2
plt.figure() 
ax1 = plt.gca()   
ax2 = plt.gca().twiny()          
pl = ax1.plot(N[25:36], -prof_N[25:36], 'b-o')
pl2 = ax2.plot(P[25:36], -prof_P[25:36],'r-o')
ax1.set_ylabel('PROF (m)', fontsize=9)
ax1.set_xlabel('NO3NO2 (µmol/kg)',fontsize=9, color='b')
ax2.set_xlabel('PO4 (µmol/kg)', fontsize=9, color='r')
ax1.xaxis.set_tick_params(color='b', labelcolor='b')
ax2.xaxis.set_tick_params(color='r', labelcolor='r')
plt.title('Profils des nitrates et des phosphates - ST K2 - 06/03/23')


