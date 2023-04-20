# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:23:13 2023

@author: leabu
"""


import matplotlib.pyplot as plt
# from datetime import timedelta
from datetime import datetime
import matplotlib.dates as dt
# import numpy.matlib as matlib
# import scipy.io as scio
# from scipy import stats
import pandas as pd
import numpy as np
# import pylab as py
# import csv as csv
import os as os
import warnings
import pickle
import h5py
# import sys
from netCDF4 import Dataset
import netCDF4

###############################################
warnings.filterwarnings("ignore")


###############################
# # CLASS Thermo:
#######################################################################
class ThermoSBE21:
    ###################################################################
    def _load(self):
        """Load a ascii file from SP2T NKE"""
        # Change comma by dot
        [adr, ext] = os.path.splitext(os.path.basename(self.filename))
        dateparsefct = lambda X: datetime.strptime(X, "%d/%m/%Y %Y\t%H:%M:%S")
        self.mydata = pd.read_table(
            self.filename,
            header=0,
            decimal=".",
            usecols=[1, 2, 7],
            names=[
                "thedate",
                "thetime",
                "Temperature"],
            parse_dates={"Date": ["thedate", "thetime"]},
            # delim_whitespace = True,
            delimiter=",",
            # skiprows=50694,
            # nrows=277424,
            skip_blank_lines=True,
            skipfooter=1)
       
       
        self.mydata["Date"] = pd.to_datetime(self.mydata["Date"], format=dateparsefct)
        self.mydata.set_index("Date", inplace=True)
        self.Level_unit = "m"
        print("-----------------------------------------------")
        print("Lecture ", adr, "............OK")
        print("-----------------------------------------------")



    ###############################
    def _loadnc(self):
        # Read Output file
       
        variable=[]
        output=[]
        xboutput= Dataset(self.filename, mode='r')
        # Load mat file and put variable in output
        print ('---------------------------------------------------------------')
        message='{:<10}{:.<30}{:.>23}'.format('Load ', self.filename, 'Ok')
        print(message)
        print ('---------------------------------------------------------------')
        for var in xboutput.variables.keys():
            variable=xboutput.variables[var]
            getattr(output,'extend')([variable])
            setattr(self, var,variable)            
            message='{:<10}{:.<30}{:.>23}'.format('Variable ', var, 'Ok')
            print(message)

    ###################################################################################
    def _savepickle(self):
        """Save everything in a pickle"""
        filenamepickle = self.filename[:-3] + "pkl"
        DataPickle = open(filenamepickle, "wb")
        pickle.dump(self, DataPickle)
        DataPickle.close()
        message = "{:<10}{:.<30}{:.>40}".format("Save:", filenamepickle, "Ok")
        print("-------------------------------------------------------------")
        print(message)
        print("-------------------------------------------------------------")

    #################################################################################################################
    def _fig2D(self, t, y, ly="labely", figname="figure.png", datef="%d %Hh"):
        """Create a 2D plot = time x variable (Hs, Pression, depth...)"""

        # Figure creation
        taille = (10, 5)  # 10*tdpi x 4*tdpi -> 1200x800 si tdpi =200
        tdpi = 200
        fig1 = plt.figure(figsize=taille)
        plt.rc("text")
        plt.rc("font", family="serif")
        lx = r"" + "Time"
        ly = r"" + ly
        plt.plot(t, y, "r")
        plt.xlabel(lx, fontsize=16)
        plt.ylabel(ly, fontsize=16)
        # plt.yaxis([2.5,3])
        plt.grid()
        date_format = dt.DateFormatter(datef)
        plt.autoscale(enable=True, axis="x", tight=True)
        plt.gca().xaxis.set_major_formatter(date_format)

        # --------------------------------------------------
        #   Save the figure
        # --------------------------------------------------
        fig1.savefig(figname, dpi=tdpi)
        message = "Figure 2D:{:<55},{:.>} dpi{:.>10}".format(
                  figname, tdpi, "Ok")
        print(message)

     
##############################################################################
##########################################################"
##                 PYTHON SCRIPT                     #####"
##########################################################"


#############################
### DEF VARIABLES
#############################
deg = "\xb0"
data_thermo = ThermoSBE21()  # File 1
data_thermo2 = ThermoSBE21()
data_thermo3 = ThermoSBE21()  # File 2
# Choose the working directory
# os.chdir()
data_thermo.filename = "20230307-000003-hydrology-TT_SBE21.ths"
data_thermo2.filename = "20230306-000003-hydrology-TT_SBE21.ths"
data_thermo3.filename="20230308-000003-hydrology-TT_SBE21.ths"


##########################################################
###              OPEN FILE                             ###
##########################################################
# # READ .TXT FILE
# data_thermo._load()  # Temp. in m
# figname = data_thermo.filename[:-4] + "_Temperature.png"
# data_thermo._fig2D(data_thermo.mydata.index[1:],
#                    data_thermo.mydata.Temperature[1:],
#                    "Temperature (degree C)", figname, "%H:%M:%S")

data_thermo._loadnc()  # Temp. in m
figname = data_thermo.filename[:-4] + "_Temperature.png"
data_thermo._fig2D(data_thermo.time [4801:9800], data_thermo.salinity[4801:9800], "Salinite (PSU)", figname, "%H:%M:%S ")


data_thermo2._loadnc()  # Temp. in m
figname2 = data_thermo2.filename[:-4] + "_Temperature.png"
data_thermo2._fig2D(data_thermo2.time [4801:9800], data_thermo2.salinity[4801:9800], "Salinite (PSU)", figname2, "%H:%M:%S ")

data_thermo3._loadnc()
figname3 = data_thermo3.filename[:-4] + "_Temperature.png"
data_thermo3._fig2D(data_thermo3.time [7200:] , data_thermo3.salinity[7200:], "Salinite (PSU)", figname3, "%H:%M:%S ")
