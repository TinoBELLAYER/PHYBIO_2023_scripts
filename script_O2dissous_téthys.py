# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:51:12 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

#ouvrir le document
f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_D_CTD_1.asc','rb')
# sauter l'en-tête
data = np.genfromtxt(f,skip_header=1)
f.close()

#choisir les colonnes correspondant aux paramètres recherchés
depth1 = -data[1:,15]
ox1 = data[1:,9]

# +11.91 correspond à l'offset sur les données
plt.plot(ox1+11.91,depth1, label="station D 06/03")
plt.xlabel('Concentration oxygène (mM/kg) ')
plt.ylabel('Depth(m)')

###########################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_D3_CTD_2.asc','rb')
data1 = np.genfromtxt(f,skip_header=1)
f.close()
ox2 = data1[1:,9]+11.91
depth2 = -data1[1:,15]
plt.plot(ox2,depth2, label="station D3 06/03")

###########################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_K_CTD_3.asc','rb')
data2 = np.genfromtxt(f,skip_header=1)
f.close()
ox3 = data2[1:,9]+11.91
depth3 = -data2[1:,15]
plt.plot(ox3,depth3, label="station K 07/03")

###########################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_K2_CTD_4.asc','rb')
data3 = np.genfromtxt(f,skip_header=1)
f.close()
ox4 = data3[1:,9]+11.91
depth4 = -data3[1:,15]
plt.plot(ox4,depth4, label="station K2 07/03")

###########################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_B_CTD_5.asc','rb')
data4 = np.genfromtxt(f,skip_header=1)
f.close()
ox5 = data4[1:,9]+11.91
depth5 = -data4[1:,15]
plt.plot(ox5,depth5, label="station B 07/03")

###########################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_D_CTD_6.asc','rb')
data5 = np.genfromtxt(f,skip_header=1)
f.close()
ox6 = data5[1:,9]+11.91
depth6 = -data5[1:,15]
plt.plot(ox6,depth6, label="station D 08/03")

###########################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_D5_CTD_7.asc','rb')
data6 = np.genfromtxt(f,skip_header=1)
f.close()
ox7 = data6[1:,9]+11.91
depth7 = -data6[1:,15]
plt.plot(ox7,depth7, label="station D5 08/03")

###########################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/V2 rapport/PHYBIO_2023_ST_D3_CTD_8.asc','rb')
data7 = np.genfromtxt(f,skip_header=1)
f.close()
ox8 = data7[1:,9]+11.91
depth8 = -data7[1:,15]
plt.plot(ox8,depth8, label="station D3 08/03")

plt.legend()