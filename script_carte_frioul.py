# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:45:27 2023

@author: Tino
"""

import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np


dataJ1 = pd.read_csv('COORDONNEES_BL_L93_J1_GT2.csv', sep=';', decimal=',')
dataJ2 = pd.read_csv('COORDONNEES_BL_L93_J2_GT3.csv', sep=';', decimal=',')
dataJ3 = pd.read_csv('COORDONNEES_BL_L93_J3_GT1.csv', sep=';', decimal=',')

f = open("LATLONG_TRANSECTS_FRIOUL_L93.csv")
coord = np.genfromtxt(f,delimiter=',',skip_header=1)
#f.close()

transectname=['TR2_0603','TR3_0603','TR4_0603','TR5_0703','TR6_0703','TR7_0803',
              'TR8_0803','TR9_0803','TR10_0803']

plt.figure(1)

i=0
coastline=gpd.read_file('tc.shp')
base=coastline.plot(color='black')
for j in transectname:
    i+=2
    df=pd.DataFrame({'Transect':j,
                 'Latitude': coord[:,i+1],
                 'Longitude':coord[:,i] })
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    gedf=gdf.set_crs("EPSG:2154")
    gdf.plot(ax=base, markersize=5, label=j)

plt.quiver(dataJ1.x,
           dataJ1.y,
           dataJ1.vit_dx,
           dataJ1.vit_dy,
           color="blue",
           scale_units="dots",
           scale=0.005,
           units='dots',
           label='Jour1 - 06/03/2023')

plt.quiver(dataJ2.x,
           dataJ2.y,
           dataJ2.vit_dx,
           dataJ2.vit_dy,
           color="red",
           scale_units="dots",
           scale=0.005,
           units='dots',
           label=('Jour2 - 07/03/2023'))

plt.quiver(dataJ3.x,
           dataJ3.y,
           dataJ3.vit_dx,
           dataJ3.vit_dy,
           color="green",
           scale_units="dots",
           scale=0.005,
           units='dots',
           label='Jour3 - 08/03/2023')

plt.text(886804.32, 6243846.97, '0.170', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886771.05, 6243917.59, '0.146', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886782.97, 6243906.99, '0.123', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886771.05, 6243911.01, '0.120', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886833.96, 6243912.38, '0.136', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886807.5, 6243876.3, '0.114', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886814.22, 6243925.79, '0.124', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886770.75, 6243925.34, '0.114', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886804.1, 6243932.54, '0.123', color='blue', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886825.29, 6243940.5, '0.072', color='red', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886808.13, 6243909.61, '0.064', color='red', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886834.41, 6243950.71, '0.057', color='red', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886863.99, 6243926.23, '0.170', color='green', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886957.4, 6243975.63, '0.033', color='green', horizontalalignment = 'left', verticalalignment = 'center')
plt.text(886859.24, 6243923.07, '0.149', color='green', horizontalalignment = 'left', verticalalignment = 'center')

plt.legend(loc='best')  

plt.show()
