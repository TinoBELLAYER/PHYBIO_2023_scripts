# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:53:38 2023

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

volmolox=22414

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_07_cast09.asc','rb')

fig1=plt.figure()

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene3=data[1:,8]
depth3=data[1:,4]
sigma3=data[1:,12]

# conversion en µmol/kg
a=oxygene3/volmolox
b=a*10**6
c=1+sigma3/1000
conc_ox3=b/c

plt.plot(conc_ox3,-depth3, label='CTD 07/03 cast09')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_07_cast11.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 07/03 cast11')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_07_cast12.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 07/03 cast12')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_07_cast13.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 07/03 cast13')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_07_cast14.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 07/03 cast14')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_07_cast15.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 07/03 cast15')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_08_008.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 08/03 cast008')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_08_010.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 08/03 cast010')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_08_011.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 08/03 cast011')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_08_012.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 08/03 cast012')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/uSBE19plus_01907708_2023_03_08_013.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene4=data[1:,8]
depth4=data[1:,4]
sigma4=data[1:,12]

a=oxygene4/volmolox
b=a*10**6
c=1+sigma4/1000
conc_ox4=b/c

plt.plot(conc_ox4,-depth4, label='CTD 08/03 cast013')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')

####################################################################################################################

f=open('/amuhome/d22001217/Documents/PHYBIO 2023/CTD OX Frioul/SBE19plus_01907708_2023_03_08_015.asc','rb')

data=np.genfromtxt(f,skip_header=1)
# f.close()

oxygene5=data[1:,8]
depth5=data[1:,4]
sigma5=data[1:,12]

a=oxygene5/volmolox
b=a*10**6
c=1+sigma5/1000
conc_ox5=b/c

plt.plot(conc_ox5,-depth5, label='CTD 08/03 cast015')
plt.xlabel('Oxygène(µM/kg)')
plt.ylabel('Depth(m)')



plt.title('PHYBIO_2023_CTD_Frioul_oxygene dissous')
plt.legend()
plt.show()