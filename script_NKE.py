# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 08:22:42 2023

@author: Benoît
"""

######################################################################################################
#                                               MODULES                                              #
######################################################################################################

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
from datetime import timedelta
from datetime import datetime
import matplotlib.dates as dt
import numpy.matlib as matlib
import scipy.io as scio
from scipy import stats
import pandas as pd
import numpy as np
import pylab as py
import csv as csv
import os as os
import warnings
import pickle
import sys


######################################################################################################
#                                         PYTHON SCRIPT                                              #
######################################################################################################
# Fonction de conversion d'hauteur NKE en pression selon Saunders (1981)

def func_h2Pa(level):
    """Converts NKE height into pressure:
    equation from Saunders, P.M. 1981
    "Practical conversion of Pressure to Depth"
    Journal of Physical Oceanography, 11, 573-574"""
    Profondeur = np.copy(level)
    c1 = 0.101
    c2 = 0.5 * 10 ** (-6)
    p = c1 * (Profondeur) + (c2 * (Profondeur) ** 2)
    p = p * 10 ** (5)
    Patmoy = 101325
    p = p + Patmoy
    message = "{:.<40}{:.>20}".format(
        "Process: NKE height into pressure", "Ok"
    )
    print(message)
    return p

######################################################################################################
# Fonction de conversion pression exprimée en PSI à Pascal

def psi_Pa(level):
   
    Profondeur = np.copy(level)
    patm = 0.07*(Profondeur)
    patm = patm * 10 ** (5)
    message = "{:.<40}{:.>20}".format(
        "Process: Baro psi into Pascal", "Ok"
    )
    print(message)
    return patm

######################################################################################################
# Relation de pression hydrostatique : permet d'exprimer les mesures en hauteur d'eau (exprimée en m)

conv_pa = (1020 * 9.81 )


######################################################################################################
# Fichier NKE

fichier_NKE="Sonde standard_33113_20230308_164241_cave.txt"               # Nom du fichier NKE
dateparse = lambda X: datetime.strptime(X, "%d/%m/%Y\t%H:%M:%S")          # Format date heure : rajouter :%f à la fin pour les microsecondes
NKE = pd.read_table(fichier_NKE,
                    encoding="ISO-8859-1",                                # Règle soucis UTF-8
                    header=4,
                    decimal=".",
                    delimiter="\s+|;",
                    usecols=[1,2, 3],
                    names=["level","thedate","thetime"],
                    parse_dates={"Date": ["thedate","thetime"]},
                    engine="python",
                    date_parser=dateparse)

NKE["level"]=func_h2Pa(NKE["level"]) # Pression mesuré par le capteur en bar
NKE["Date"] = pd.to_datetime(NKE["Date"])

######################################################################################################
# Fichier Barologger

fichier_atm = "baro_08032023.csv"                                         # Nom du fichier Barologger
dateparse = lambda X: datetime.strptime(X,"%d/%m/%Y\t%H:%M:%S")
baro = pd.read_table(fichier_atm,
                      encoding="ISO-8859-1",
                      header=11,
                      decimal=".",
                      usecols=[0,1,3],
                      names=["thedate", "thetime","level"],
                      parse_dates={"Date": ["thedate","thetime"]},
                      date_parser=dateparse,
                      delimiter=",",
                      engine="python",
                      skip_blank_lines=True)
baro["level"]=baro["level"]*0.07*10**(5) #conversion psi en bar
baro=baro.set_index("Date")

######################################################################################################
# Interpolation barologger

upsampled = baro.resample("4S")                                          # Fréquence d'échantillonnage du capteur NKE pour interpoler avec le barologger
baro_interpolated = upsampled.interpolate()
atm = baro_interpolated["level"]  
t1=py.datetime.datetime(*(2023, 3, 8, 15, 37, 0))                        # t1 et t2 correspond au début et fin de la mesure NKE
t2=py.datetime.datetime(*(2023, 3, 8, 16, 32, 0))
baro_interpolated_selec = baro_interpolated.query("Date > @t1 and Date <= @t2")
NKE_selec = NKE.query("Date > @t1 and Date <= @t2")

######################################################################################################
# Calcul facteur de correction de la callibration

t3=py.datetime.datetime(*(2023, 3, 8, 14, 58, 0))                        # t3 et t4 correspond au début et fin du premier palier des NKE
t4= py.datetime.datetime(*(2023, 3, 8, 14, 59, 0))
baro_interpolated_selec1 = baro_interpolated.query("Date > @t3 and Date <= @t4")
NKE_selec1 = NKE.query("Date > @t3 and Date <= @t4")
Pal1=(NKE_selec1["level"].to_numpy()-baro_interpolated_selec1["level"].to_numpy())/conv_pa

t5=py.datetime.datetime(*(2023, 3, 8, 15, 1, 0))                         # t5 et t6 correspond au début et fin du deuxième palier des NKE
t6= py.datetime.datetime(*(2023, 3, 8, 15, 2, 0))
baro_interpolated_selec2 = baro_interpolated.query("Date > @t5 and Date <= @t6")
NKE_selec2 = NKE.query("Date > @t5 and Date <= @t6")
Pal2=(NKE_selec2["level"].to_numpy()-baro_interpolated_selec2["level"].to_numpy())/conv_pa

t7=py.datetime.datetime(*(2023, 3, 8, 15, 4, 0))                         # t7 et t8 correspond au début et fin du troisième palier des NKE
t8= py.datetime.datetime(*(2023, 3, 8, 15, 5, 0))
baro_interpolated_selec3 = baro_interpolated.query("Date > @t7 and Date <= @t8")
NKE_selec3 = NKE.query("Date > @t7 and Date <= @t8")
Pal3=(NKE_selec3["level"].to_numpy()-baro_interpolated_selec3["level"].to_numpy())/conv_pa


corr1 = np.absolute(Pal1.mean()-0.095)                                   # Remplacer par la première mesure de palier mesuré (en m)
corr2 = np.absolute(Pal2.mean()-0.18)                                    # Remplacer par la deuxième mesure de palier mesuré (en m)
corr3 = np.absolute(Pal3.mean()-0.29)                                    # Remplacer par la troisième mesure de palier mesuré (en m)
correction = corr1 + corr2 + corr3 /3                                    # Moyenne des corrections pour chaque palier

######################################################################################################
# Calcul Hauteur d"eau corrigé de la pression atmospherique

Patm_cor=(NKE_selec["level"].to_numpy()-baro_interpolated_selec["level"].to_numpy())/conv_pa

######################################################################################################
# Calcul Hauteur d"eau corrigé de la pression atmospherique et de la callibration
Pcal_cor=Patm_cor - correction                                           # Tiens compte de la Patm et de la calibration pour les mesures NKE
                                                                         # Vérifier s'il faut corriger + ou - avec la correction selon les valeurs notés 0 l'aide du sondeur

######################################################################################################
# Calibration 

P1 = NKE.query("Date > @t3 and Date <= @t4")
P2 = NKE.query("Date > @t5 and Date <= @t6")
P3 = NKE.query("Date > @t7 and Date <= @t8")

##################################################

B1 =  baro_interpolated.query("Date > @t3 and Date <= @t4")
B2 =  baro_interpolated.query("Date > @t5 and Date <= @t6")
B3 =  baro_interpolated.query("Date > @t7 and Date <= @t8")

##################################################

P1_corr = (P1["level"] - B1["level"].to_numpy()) /conv_pa -corr1         # Vérifier s'il faut corriger + ou - avec la correction selon les valeurs notés de la calibration
P2_corr = (P2["level"] - B2["level"].to_numpy()) /conv_pa -corr2
P3_corr = (P3["level"] - B3["level"].to_numpy()) /conv_pa -corr3

##################################################

P1_corr_mean = P1_corr.mean()                                            # Mesure d'un point moyen d'hauteur d'eau pour chaque palier
P2_corr_mean = P2_corr.mean()
P3_corr_mean = P3_corr.mean()

##################################################

tP1_mean = P1["Date"].mean()                                             # Mesure d'un point moyen de la date pour chaque palier
tP2_mean = P2["Date"].mean()
tP3_mean = P3["Date"].mean()

######################################################################################################
# Figure de la calibration

plt.figure(1,figsize=(10,4))
plt.title("Calibration du capteur NKE-33113 : Hauteur d'eau corrigée de la hauteur équivalente à la pression atmosphérique", fontsize = 18)
Dt = mdates.DateFormatter("%d/%m %H:%M")
plt.gca().xaxis.set_major_formatter(Dt)
plt.plot(P1["Date"],P1_corr, "k_", linewidth=6)
plt.plot(P2["Date"],P2_corr, "k_", linewidth=6)
plt.plot(P3["Date"],P3_corr, "k_", linewidth=6)
plt.xlabel("Temps", fontsize = 16)
Dt = mdates.DateFormatter("%H:%M")
plt.gca().xaxis.set_major_formatter(Dt)
plt.ylabel("Hauteur (m)",fontsize = 16)
plt.gca().yaxis.set_tick_params(labelsize = 15)
plt.gca().xaxis.set_tick_params(labelsize = 15)

##################################################

plt.plot(tP1_mean,P1_corr_mean, "ro")
plt.plot(tP2_mean,P2_corr_mean, "ro")
plt.plot(tP3_mean,P3_corr_mean, "ro")

##################################################

plt.xlabel("Temps")
plt.ylabel("Hauteur (m)")
plt.show()

######################################################################################################
# Figures avant et après correction de la pression atmosphérique et de la calibration

fig2 = plt.figure(2,figsize=(10,4))
plt.subplot(311)
plt.plot(NKE_selec["Date"],NKE_selec["level"]/conv_pa, 'k-')
# plt.xlabel("Temps")
# Dt = mdates.DateFormatter("%d/%m %H:%M")
# plt.gca().xaxis.set_major_formatter(Dt)
ax =plt.gca()
ax.get_xaxis().set_visible(False)
plt.ylabel("Hauteur (m)",fontsize = 14)
plt.gca().yaxis.set_tick_params(labelsize = 15)
plt.title("Hauteur d'eau sans correction", fontsize = 18)

##################################################

plt.subplot(312)
plt.plot(NKE_selec["Date"],Patm_cor, 'k-')
# plt.xlabel("Temps")
# Dt = mdates.DateFormatter("%d/%m %H:%M")
# plt.gca().xaxis.set_major_formatter(Dt)
ax =plt.gca()
ax.get_xaxis().set_visible(False)
plt.gca().yaxis.set_tick_params(labelsize = 15)
plt.ylabel("Hauteur (m)",fontsize = 16)
plt.title("Hauteur d'eau après correction de la pression atmosphérique", fontsize = 18)

##################################################

plt.subplot(313)
plt.plot(NKE_selec["Date"],Pcal_cor, 'k-')
plt.xlabel("Temps", fontsize = 16)
Dt = mdates.DateFormatter("%H:%M")
plt.gca().xaxis.set_major_formatter(Dt)
plt.ylabel("Hauteur (m)",fontsize = 16)
plt.title("Hauteur d'eau après correction de la pression atmosphérique et de la callibration", fontsize = 18)
plt.gca().yaxis.set_tick_params(labelsize = 15)
plt.gca().xaxis.set_tick_params(labelsize = 15)
fig2.tight_layout()

######################################################################################################