#!/usr/bin/python
# coding: utf-8
#############################################"    
##                 MODULE               #####"
#############################################"
import matplotlib.gridspec as gridspec
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

plt.close('all')
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
class ADCP(object):
###################################################################################   
    def load_ADCP(self):
        attrs = "depth_cell_length", "blank_after_transmit", "depth_from_config", \
        "number_depth_cells", "pings_per_ensemble", "time_per_ensemble", \
        "profiling_mode"
        num = 0
        ensemble_attrs = {1: ("year", "month", "day", "hour","minute","second","hundredths",
                          "number", "num_ensembles","pitch","roll","corrected_heading","temperature"),
                      2: ("velocity_east","velocity_west","velocity_up","velocity_error",\
                          "bottom_depth", "altitude","delta_altitude","HDOP",
                          "depth1","depth2","depth3","depth4"),
                      3: ("elapsed_distance","elapsed_time","distance_north","distance_east",\
                          "distance_good"),
                      4: ("latitude","longitude","invalid","unused"),
                      5: ("discharg_mid","discharge_top","discharge_bot", \
                          "start_discharge","start_dist","end_discharge","end_dist",\
                          "start_depth","end_depth"),
                      6: ("num_bins","unit","velocity_ref","intensity_units",\
                          "intensity_scale","sound_absorption")
                    }
            
        #self.bscmoy = (self.cell_bsc1+self.cell_bsc2+self.cell_bsc3+self.cell_bsc4)/4

        self.bin_attrs = ["depthcell", "velocity", "azimuth", "east", "north", "up", "error", "bsc1",\
             "bsc2", "bsc3", "bsc4", "percent_good", "discharge"]
        
        #----------------------
        # Read the file
        #----------------------
        with open(self.filename, 'r') as f:
            lines = [i[:-1] for i in f.readlines()]
            vals = self.split_line(lines.pop(0))
            vals = self.split_line(lines.pop(0))
            vals = self.split_line(lines.pop(0))
        #----------------------------------------------
        # Mise en place des variables sur l'object self
        #----------------------------------------------
        for attr_tup in ensemble_attrs.values():
            for i in range(len(attr_tup)):
                exec('self.'+ str(attr_tup[i])+'=[]')
        for i in range(len(attrs)):
            setattr(self, attrs[i], vals[i])    
        for i in self.bin_attrs :
            exec('self.cell_'+i+'=np.array([])')
            
        #--------------------------------------
        # Attribution des valeurs aux variables
        #--------------------------------------
        while len(lines):
            #####################################
            # Read the header for each ensemble ==> ensemble_attrs
            for attr_tup in ensemble_attrs.values():
                vals = self.split_line(lines.pop(0)) 
                for i in range(len(attr_tup)):                   
                    try:
                        exec('self.'+ str(attr_tup[i])+'.append('+str(vals[i])+")")
                    except:
                        exec('self.'+ str(attr_tup[i])+'.append("'+str(vals[i])+'")')
            #####################################
            # Read the data for each ensemble ==> bin_attrs
            for i in self.bin_attrs :
                exec('cell_'+i+'=np.array([])')
            for i in range(self.num_bins[0]):                
                vals=self.split_line(lines.pop(0))
                for j,k in zip(self.bin_attrs,vals):
                    exec ('cell_'+str(j)+'=np.append(cell_'+str(j)+','+str(k)+')')
                
            for j in self.bin_attrs:
                exec ('self.cell_'+str(j)+'=np.append(self.cell_'+str(j)+',cell_'+str(j)+')')
                
        # Reshape        
        for j in self.bin_attrs:
            exec ('self.cell_'+str(j)+'=self.cell_'+str(j)+'.reshape(int(len(self.cell_'+str(j)+')/self.num_bins[0]),self.num_bins[0])')
    
         
###############################################################################
    def split_line(self,line):
        # Convert to float or int, as appropriate
        makenum = lambda x: float(x) if x.find('.') != -1 else int(x)
        # Test for string, call makenum if not string
        isstring = lambda x: x if x.isalpha() else makenum(x)
        return [i for i in map(isstring,line.split())]
    
    
###############################################################################
    def calcul(self):
        self.bsc=[(self.cell_bsc1[i]+self.cell_bsc2[i]+self.cell_bsc3[i]+self.cell_bsc4[i])/4 for i in range(len(self.cell_bsc1))]
        self.depth=[(self.depth1[i]+self.depth2[i]+self.depth3[i]+self.depth4[i])/4 for i in range(len(self.depth1))]
        self.deepblanking=  [math.cos(20*math.pi/180)*self.depth[i] for i in range(len(self.depth))]# zone de champs lointain cos
        for i in self.bin_attrs:
            exec('self.cell_'+i+'[np.where(self.cell_'+i+'==-32768)]=np.nan')


###############################################################################
    def ping10(self):
        cell_velocity=np.copy(self.cell_velocity)
        cell_azimuth=np.copy(self.cell_azimuth)
        # MOYENNE SUR 10 PINGS DES DONNEES DE VITESSE #########################
        self.mean_velocity = np.ones(np.shape(cell_velocity))
        for j in range(len(cell_velocity[0])): 
            i=0         # all along the row
            while i <= len(cell_velocity[:,j]):    # all along the column    
                M = cell_velocity[i:i+10,j]  #,j:j+17]  # meaning 1x10-bin cell
                moy = np.nanmean(M)
                for k in range(len(M)):
                    if M[k] != np.nan :
                        M[k] = moy
                    else:
                        M[k]=np.nan
                    self.mean_velocity[i:i+10,j]= np.array(M)  
                i=i+10
    
        # MOYENNE SUR 10 PINGS DES DONNEES DE DIRECTION #######################
        self.mean_azimuth = np.ones(np.shape(cell_azimuth))        
        for j in range(len(cell_azimuth[0])): 
            i=0         # all along the row
            while i <= len(cell_azimuth[:,j]):    # all along the column    
                M2 = cell_azimuth[i:i+10,j]  #,j:j+17]  # meaning 1x10-bin cell
                moy = np.nanmean(M2)
                for k in range(len(M2)):
                    if M2[k] != np.nan :
                        M2[k] = moy
                    else:
                        M2[k]=np.nan
                    self.mean_azimuth[i:i+10,j]= np.array(M2)  
                i=i+10     

###############################################################################
    def plot10pingADCP(self):
        
        # Data preparation
        y=self.cell_depthcell[0,:]
        z=self.depth
        
        for i in ['velocity','azimuth']:
            exec('self.Z=np.transpose(self.mean_'+i+'.copy())')
            #Z=np.transpose(Zi)
            Zmask=np.ma.masked_where(np.isnan(self.Z)==1, self.Z)
            x=self.elapsed_distance
            X, Y = np.meshgrid(x, y)

            # Figure creation
            taille = (8,4) # 10*tdpi x 4*tdpi -> 1200x800 si tdpi =200
            tdpi=200
            gs = gridspec.GridSpec(1, 1)
            fig, (ax1) = plt.subplots(1,1,figsize =taille, dpi=tdpi,sharex=True)
            ax1 = plt.subplot(gs[0, :])
            plt.rc('text', usetex=True)
            plt.rc('font', family='serif')
            # ---------------------           
            # subplot 1
            graf1=ax1.pcolor(X,Y, Zmask, vmin=0, vmax=360,cmap='twilight_shifted') # to change if velocity
            #ax1.hold
            try:
                ax1.plot(x,z, linewidth=4, color='k')
                ax1.plot(x,self.deepblanking,'--', linewidth=1, color='k')
            except:
                x2=self.elapsed_distance
                ax1.plot(x2,z, linewidth=4, color='k')
                ax1.plot(x2,self.deepblanking,'--', linewidth=1, color='k')
            ax1.invert_yaxis()
            cb=fig.colorbar(graf1, ax=ax1,orientation='vertical')
            cb.ax.tick_params(labelsize=8) 
            cb.set_label(str(i)+'(moyennée sur 10 bins) [degrés]',fontsize=10)   
            #ax1.set_title(str(i).replace('_', ' '), fontsize=18, color='gray')
            
            ax1.set_ylabel(r'Profondeur [m]', fontsize=10)
            ax1.set_xlabel(r'Distance transect [m]', fontsize=10)
            
            ax1.yaxis.set_tick_params(labelsize = 8)
            ax1.xaxis.set_tick_params(labelsize = 8)
            ax1.autoscale(enable=True, axis='both', tight=True)
            #plt.tight_layout

           
            # Output figure in 'png'
            
            figname=self.filename+i+'.png'
            print ('Figure :', figname, ' :', tdpi,' dpi......Ok'  ) 
            fig.savefig(figname, dpi=tdpi)
            
            # !!! TO DISPLAY ONLY 1 VARIABLE
            #if i != "azimuth":   # Change variable name here
            #plt.close(fig)

###############################################################################
    def figureADCP(self):
        
        # Data preparation
        y=self.cell_depthcell[0,:]
        z=self.depth
        
        for i in self.bin_attrs:
            exec('self.Z=np.transpose(self.cell_'+i+'.copy())')
            #Z=np.transpose(Zi)
            Zmask=np.ma.masked_where(np.isnan(self.Z)==1, self.Z)
            x=self.elapsed_distance
            X, Y = np.meshgrid(x, y)

            # Figure creation
            taille = (8,4) # 10*tdpi x 4*tdpi -> 1200x800 si tdpi =200
            tdpi=200
            gs = gridspec.GridSpec(1, 1)
            fig, (ax1) = plt.subplots(1,1,figsize =taille, dpi=tdpi,sharex=True)
            ax1 = plt.subplot(gs[0, :])
            plt.rc('text', usetex=True)
            plt.rc('font', family='serif')
            # ---------------------           
            # subplot 1
            graf1=ax1.pcolor(X,Y, Zmask, vmin=0, vmax=360)
            #ax1.hold
            try:
                ax1.plot(x,z, linewidth=4, color='k')
                ax1.plot(x,self.deepblanking,'--', linewidth=1, color='k')
            except:
                x2=self.elapsed_distance
                ax1.plot(x2,z, linewidth=4, color='k')
                ax1.plot(x2,self.deepblanking,'--', linewidth=1, color='k')
            ax1.invert_yaxis()
            cb=fig.colorbar(graf1, ax=ax1,orientation='vertical')
            cb.ax.tick_params(labelsize=8) 
            cb.set_label('Direction du courant [degrés]',fontsize=10) #cb.set_label(str(i).replace('_',' '),fontsize=10)   
            #ax1.set_title(str(i).replace('_', ' '), fontsize=18, color='gray')
            
            ax1.set_ylabel(r'Profondeur [m]', fontsize=10)
            ax1.set_xlabel(r'Distance transect [m]', fontsize=10)
            
            ax1.yaxis.set_tick_params(labelsize = 8)
            ax1.xaxis.set_tick_params(labelsize = 8)
            ax1.autoscale(enable=True, axis='both', tight=True)
            #plt.tight_layout

           
            # Output figure in 'png'
            
            figname=self.filename+i+'.png'
            print ('Figure :', figname, ' :', tdpi,' dpi......Ok'  ) 
            fig.savefig(figname, dpi=tdpi)
            
            # !!! TO DISPLAY ONLY 1 VARIABLE
            #if i != "azimuth":   # Change variable name here
            plt.close(fig)

###############################################################################                
    def meanbscADCP(self):
        
        # Data preparation
        y=self.cell_depthcell[0,:]
        z=self.depth
        
        exec('self.Z=np.transpose(self.bsc.copy())')
        #Z=np.transpose(Zi)
        Zmask=np.ma.masked_where(np.isnan(self.Z)==1, self.Z)
        x=self.elapsed_distance
        X, Y = np.meshgrid(x, y)

        # Figure creation
        taille = (8,4) # 10*tdpi x 4*tdpi -> 1200x800 si tdpi =200
        tdpi=200
        gs = gridspec.GridSpec(1, 1)
        fig, (ax1) = plt.subplots(1,1,figsize =taille, dpi=tdpi,sharex=True)
        ax1 = plt.subplot(gs[0, :])
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        # ---------------------           
        # subplot 1
        graf1=ax1.pcolor(X,Y, Zmask, vmin=0, vmax=100)
        #ax1.hold
        try:
            ax1.plot(x,z, linewidth=4, color='k')
            ax1.plot(x,self.deepblanking,'--', linewidth=1, color='k')
        except:
            x2=self.elapsed_distance
            ax1.plot(x2,z, linewidth=4, color='k')
            ax1.plot(x2,self.deepblanking,'--', linewidth=1, color='k')
        ax1.invert_yaxis()
        cb=fig.colorbar(graf1, ax=ax1,orientation='vertical')
        cb.ax.tick_params(labelsize=8) 
        cb.set_label("Rétrodiffusion moyenne [pourcent]",fontsize=10)
        #ax1.set_title("Mean BackScatter (%)", fontsize=18, color='gray')
        
        ax1.set_ylabel(r'Profondeur [m]', fontsize=10)
        ax1.set_xlabel(r'Distance transect [m]', fontsize=10)
        
        ax1.yaxis.set_tick_params(labelsize = 8)
        ax1.xaxis.set_tick_params(labelsize = 8)
        ax1.autoscale(enable=True, axis='both', tight=True)
        #plt.tight_layout
       
        # Output figure in 'png'
        
        figname=self.filename+'mean_bsc.png'
        print ('Figure :', figname, ' :', tdpi,' dpi......Ok'  ) 
        fig.savefig(figname, dpi=tdpi)
        
        plt.close(fig)
       

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

#############################################"    
##             PYTHON SCRIPT            #####"
#############################################"

####################################################################################################################
                                                                      
#############################
### DEF VARIABLES
############################# 

adcp= ADCP()

##########################################################  
###              OPEN FILE                             ###
##########################################################
# Choose the working directory

#os.chdir('../')


##########################################################  
###              OPEN FILE                             ###
##########################################################  
adcp.filename='ADCP_07032023/GROUPE3_002t.000'
#adcp.filename='ADCP_08032023/RHO_004t.000'
############################# 
### READ FILE
############################# 
adcp.load_ADCP()
adcp.calcul()
adcp.ping10()
 

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

#############################
##          OUTPUT         ##
#############################

#%%
print ('-----------------------------------------------------')
print ('    OUTPUT:')
print ('-----------------------------------------------------')

############################

## Figures 2 D
adcp.plot10pingADCP()
print('------------------------------------------------------')
#adcp.figureADCP()
print('------------------------------------------------------')
#adcp.meanbscADCP()
                                                                      #      
                                                                     ###                  
                                                                    # # #
                                                                      #
                                                                      #
########################################################################################################################################################## 
#       import pdb; pdb.set_trace()

