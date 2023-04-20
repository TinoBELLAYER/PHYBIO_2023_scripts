# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:13:46 2023

@author: leabu
"""

import numpy as np
import gsw
import matplotlib.pyplot as plt
import pandas as pd
 
# Extract data from file *********************************
# f = open('CTD_profile.csv', 'r')
f = 'PHYBIO_2023_ST_K2_CTD_4_07.asc'

mydata = pd.read_csv(f,
                     header=1,                    
                     sep="\s+",
                     decimal=".",
                     usecols=[21, 22],
                     names=["salt" , "temp"],
                     encoding="ISO-8859-1")

 

# Figure out boudaries (mins and maxs)
smin =mydata.salt.min() - (0.01 * mydata.salt.min())
smax = mydata.salt.max() + (0.01 * mydata.salt.max())
tmin = mydata.temp.min() - (0.1 * mydata.temp.max())
tmax =mydata.temp.max() + (0.1 * mydata.temp.max())

 
# Calculate how many gridcells we need in the x and y dimensions
xdim = int(round((smax-smin)/0.1+1,0))
ydim = int(round((tmax-tmin)+1,0))
 
# Create empty grid of zeros
dens = np.zeros((ydim,xdim))
 
# Create temp and salt vectors of appropiate dimensions
ti = np.linspace(1,ydim-1,ydim)+tmin
si = np.linspace(1,xdim-1,xdim)*0.1+smin
 
# Loop to fill in grid with densities
for j in range(0,int(ydim)):
    for i in range(0, int(xdim)):
        dens[j,i]=gsw.sigma0(si[i],ti[j])
 
# Substract 1000 to convert to sigma-t
#dens = dens - 1000
 
# Plot data ***********************************************
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
CS = plt.contour(si,ti,dens, linestyles='dashed', colors='k')
plt.clabel(CS, fontsize=12, inline=1, fmt='%0.1f') # Label every second level
 
ax1.plot(mydata.salt,mydata.temp,'k',markersize=9,label='ST_K2')


ax1.set_xlabel('Salinité(PSU)')
ax1.set_ylabel('Température (°C)')
ax1.set_ylim(12.8,14)



#------------St B-----------------
f2='PHYBIO_2023_ST_B_CTD_5_07.asc'
mydata2 = pd.read_csv(f2,
                      header=1,                    
                      sep="\s+",
                      decimal=".",
                      usecols=[21, 22],
                      names=["salt" , "temp"],
                      encoding="ISO-8859-1")

ax1.plot(mydata2.salt,mydata2.temp,'r',markersize=9, label='ST_B')



#----ST_D_06--------------------
f3='PHYBIO_2023_ST_D_CTD_1_06.asc'
mydata3 = pd.read_csv(f3,
                      header=1,                    
                      sep="\s+",
                      decimal=".",
                      usecols=[21, 22],
                      names=["salt" , "temp"],
                      encoding="ISO-8859-1")

ax1.plot(mydata3.salt,mydata3.temp,markersize=9, label='ST_D 06_03')


#-----------ST_D_08------------------------
f4='PHYBIO_2023_ST_D_CTD_6.asc'
mydata4 = pd.read_csv(f4,
                      header=1,                    
                      sep="\s+",
                      decimal=".",
                      usecols=[21, 22],
                      names=["salt" , "temp"],
                      encoding="ISO-8859-1")

ax1.plot(mydata4.salt,mydata4.temp,markersize=9, label='ST_D 08_03')

#--------------------- ST_D3_06-----------------

f5='PHYBIO_2023_ST_D3_CTD_2_06.asc'
mydata5 = pd.read_csv(f5,
                      header=1,                    
                      sep="\s+",
                      decimal=".",
                      usecols=[21, 22],
                      names=["salt" , "temp"],
                      encoding="ISO-8859-1")

ax1.plot(mydata5.salt,mydata5.temp,markersize=9, label='ST_D3 06_03')

#--------------------- ST_D3_08-----------------

f6='PHYBIO_2023_ST_D3_CTD_8.asc'
mydata6 = pd.read_csv(f6,
                      header=1,                    
                      sep="\s+",
                      decimal=".",
                      usecols=[21, 22],
                      names=["salt" , "temp"],
                      encoding="ISO-8859-1")

ax1.plot(mydata6.salt,mydata6.temp,markersize=9, label='ST_D3 08_03')


#-----ST_D5------------

f6='PHYBIO_2023_ST_D5_CTD_7.asc'
mydata6 = pd.read_csv(f6,
                      header=1,                    
                      sep="\s+",
                      decimal=".",
                      usecols=[21, 22],
                      names=["salt" , "temp"],
                      encoding="ISO-8859-1")

ax1.plot(mydata6.salt,mydata6.temp,markersize=9, label='ST_D5')

#-----ST_K------------

f7='PHYBIO_2023_ST_K_CTD_3_07.asc'
mydata7 = pd.read_csv(f7,
                      header=1,                    
                      sep="\s+",
                      decimal=".",
                      usecols=[21, 22],
                      names=["salt" , "temp"],
                      encoding="ISO-8859-1")

ax1.plot(mydata7.salt,mydata7.temp,markersize=9, label='ST_K')

plt.plot (39.0, 14,"ro", label ="LIW")
plt.ylim (12.8,14.1)
plt.legend ()
plt.show()