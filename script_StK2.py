# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:19:08 2023

@author: leabu
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------St D_06-----------
fich = open('PHYBIO_2023_ST_K2_CTD_4_07.asc', 'rb') #npm du fichier

data_D = np.genfromtxt(fich, skip_header=1) #enlever le header
fich.close()

temp_D = data_D[1:, 14] #choisir la bonne colonne du fichier
prof_D = data_D[1:, 15]
plt.plot(temp_D, -prof_D)#plot le graphe 


plt.ylim(-100,0) #coupé l'axe x
plt.xlabel ('PAR(µEinstein/m²/s-1)') #titre axe
plt.ylabel('Profondeur (m)')

plt.subplot(231) #pour plotter plusieurs graphe à la suite

# --------------St D_06-----------
fich = open('PHYBIO_2023_ST_K2_CTD_4_07.asc', 'rb')

data_D = np.genfromtxt(fich, skip_header=1)
fich.close()

temp_D = data_D[1:, 7]
prof_D = data_D[1:, 15]
#plt.ylim (-150,0)
plt.plot(temp_D, -prof_D, label='06_03_2023')



plt.xlabel ('Température (°C)')
plt.ylabel('Profondeur (m)')



plt.subplot(232)
# --------------St D_08-----------
fich = open('PHYBIO_2023_ST_K2_CTD_4_07.asc', 'rb')

data_D = np.genfromtxt(fich, skip_header=1)
fich.close()

temp_D = data_D[1:, 16]
prof_D = data_D[1:, 15]
plt.plot(temp_D, -prof_D, label='08_03_2023')
plt.xlabel ('salinité (PSU)')




plt.subplot (233)
# --------------St D_08-----------
fich = open('PHYBIO_2023_ST_K2_CTD_4_07.asc', 'rb')

data_D = np.genfromtxt(fich, skip_header=1)
fich.close()

temp_D = data_D[1:, 17]
prof_D = data_D[1:, 15]
plt.plot(temp_D, -prof_D, label='08_03_2023')
plt.xlabel ('Sigma (Kg/m^3)')



plt.subplot (234)
# --------------St D_08-----------
fich = open('PHYBIO_2023_ST_K2_CTD_4_07.asc', 'rb')

data_D = np.genfromtxt(fich, skip_header=1)
fich.close()

temp_D = data_D[1:, 13]
prof_D = data_D[1:, 15]
plt.ylim (-600,0)
plt.plot(temp_D, -prof_D, label='08_03_2023')

plt.xlabel ('Transmission (%)')
plt.ylabel ('Profondeur (m)')



plt.subplot (235)
# --------------St D_08-----------
fich = open('PHYBIO_2023_ST_K2_CTD_4_07.asc', 'rb')

data_D = np.genfromtxt(fich, skip_header=1)
fich.close()

temp_D = data_D[1:, 12]
prof_D = data_D[1:, 15]
plt.plot(temp_D, -prof_D, label='08_03_2023')
plt.ylim (-600,0)

plt.xlabel ('Fluorescence (µg/L)')
plt.ylabel ('Profondeur (m)')



plt.subplot (236)
# --------------St D_08-----------
fich = open('PHYBIO_2023_ST_K2_CTD_4_07.asc', 'rb')
data_D = np.genfromtxt(fich, skip_header=1)
fich.close()
temp_D = data_D[1:, 9]
prof_D = data_D[1:, 15]
plt.plot(temp_D+11.91, -prof_D, label='08_03_2023')
plt.ylim (-600,0)
plt.xlabel ('oxygène (µmol/Kg')




