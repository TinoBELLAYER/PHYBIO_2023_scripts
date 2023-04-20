#!/usr/bin/python
# coding: utf-8
#############################################"    
##                 MODULE               #####"
#############################################"
import matplotlib.pyplot as plt
from tkinter import filedialog
from datetime import datetime
import numpy.matlib as matlib
import matplotlib.dates as dt
import scipy.stats as stat
import tkinter as Tk
import pandas as pd
import numpy as np
import pylab as py
import scipy.io
import pickle
import math
import sys
import os
                                                                      #      
                                                                     ###                  
                                                                    # # #
                                                                      #
                                                                      #
##########################################################################################################################################################  
                                                                      #
                                                                      #
                                                                    # # #
                                                                     ###         
                                                                      #


class meteo(object):
#############################################################
    def _load_solinst(self, filename):
        """ OPEN AND READ A FILE FROM SOLINST BAROLOGGER , VERSION PANDA """     
        dateparse = lambda X: datetime.strptime(X,'%d/%m/%Y \t%H:%M:%S')                                               
        self.mydata = pd.read_table(self.filename,header=11, 
                            decimal='.',
                            usecols=[0,1,3],
                            names=["thedate","thetime","Pressure"],
                            parse_dates={"Date": ["thedate","thetime"]},
                            date_parser=dateparse,
                            #delim_whitespace = True,
                            delimiter=',',
                            #skiprows=100202,
                            #nrows=2537035,
                            skip_blank_lines=True,
                            encoding='Latin-1')
        self.mydata.set_index('Date', inplace=True)
#############################################################
    def _figuremeteo(self, y, text):
        # Figure creation
        taille = (10,5) # 10*tdpi x 4*tdpi -> 1200x800 si tdpi =200
        tdpi=200
        fig1=plt.figure(figsize=taille)
        ax = fig1.add_subplot(111)
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(self.mydata.index,y, 'r.')    
        plt.xlabel(r'Time', fontsize=16)
        plt.ylabel(text, fontsize=16)
        date_format = dt.DateFormatter('%y/%m/%d %H:%M:%S')
        plt.gca().xaxis.set_major_formatter(date_format)
        plt.xticks(rotation=45)
        plt.autoscale(enable=True, axis='both', tight=True)
        plt.tight_layout()
        #--------------------------------------------------
        #   Save the figure
        #--------------------------------------------------
        
        figname=self.adr+ '_'+text+ '.png'                         
        fig1.savefig(figname,dpi=tdpi)
        print( 'Figure :', figname, ' :', tdpi,' dpi......Ok')
        #plt.show()
#############################
### DEF VARIABLES
############################# 
deg = u'\xb0'
AtmoP=meteo()

##########################################################  
###              OPEN FILE                             ###
##########################################################  

root=Tk.Tk()
root.update()
# Choose the working directory

# os.chdir('../../../../workspace/marseille/Barologger')
AtmoP.filename = filedialog.askopenfilename(title="Ouvrir un fichier barolog solinst",
                           filetypes=[('solinst files','.csv'),('all files','.*')])
rep=os.path.dirname(AtmoP.filename)

[AtmoP.adr, ext]=os.path.splitext(os.path.basename(AtmoP.filename))
try:
    os.mkdir(AtmoP.adr)
except:
    pass
os.chdir(AtmoP.adr)
root.destroy()

# Read File
AtmoP._load_solinst(AtmoP.filename)

# Convert into HPa
AtmoP.mydata['Pressure']= 68.947572932 *AtmoP.mydata['Pressure']
# Figures
AtmoP._figuremeteo(AtmoP.mydata.Pressure,'Atmospheric Pressure (HPa)')
# AtmoP._figuremeteo(AtmoP.mydata.Temperature,'Atmospheric Temperature (degree C)')


