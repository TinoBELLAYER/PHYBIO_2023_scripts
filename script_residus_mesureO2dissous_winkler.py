# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:55:31 2023

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(color_codes=True)
plt.rcParams["figure.figsize"]=[12,12]

np.random.seed(0)

f=open('résidus tethys.csv','rb')

data=np.genfromtxt(f,skip_header=1)

oxygenetethys=data[1:,2]
oxygenewinkler=data[1:,1]
depth=data[1:,0]
difference=data[1:,3]

##############################################################################################

fig1=plt.figure()
plt.plot(oxygenewinkler,oxygenetethys, 'ok')
plt.xlabel('Oxygène Winkler (mM/kg)')
plt.ylabel('Oxygène Téthys (mM/kg)')

x = oxygenewinkler[:, np.newaxis]
y = oxygenetethys[:, np.newaxis]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
 
model.fit(x,y)
y_predict = model.predict(x)

print(f"intercept:{model.intercept_}")
print(f"slope:{model.coef_}")
plt.scatter(x, y)
plt.plot(x, y_predict, color='k')

#plt.axis([0,250,0,240])

###############################################################################################

fig2=plt.figure()
plt.plot(difference, -depth, 'ok')
plt.ylabel('Profondeur (m)')
plt.xlabel('Oxygène Winkler - Oxygène téthys (mM/kg)')

moy=np.mean(difference)
print('résidus = ',moy)
plt.axvline(x=moy,color='k',linestyle='-')


plt.plot()
plt.legend()
plt.show()