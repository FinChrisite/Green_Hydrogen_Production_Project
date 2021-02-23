# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:36:36 2020

@author: Fin Christie
"""

import pandas as pd
import numpy as np
import statistics as statistics
import matplotlib.pyplot as plt
import datetime as dt

Months = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']

df =  pd.read_csv (r"C:\Users\Fin Christie\Documents\Uni\4th Year\EM401\Data\Windfarm_Data_Analysis.csv")
date_time_stamp = df['local_time'].tolist()
Bea_Out_Hourly = df['Beatrice'].tolist()
Kil_Out_Hourly = df['Kilbraur'].tolist()
Syn_Out_Hourly = df['synth'].tolist()

def average_monthly(hourly_data):
    monthly_Av = []
    
    monthly_Av.append(statistics.mean(hourly_data[0:744]))
    monthly_Av.append(statistics.mean(hourly_data[744:1416]))
    monthly_Av.append(statistics.mean(hourly_data[1416:2160]))
    monthly_Av.append(statistics.mean(hourly_data[2160:2880]))
    monthly_Av.append(statistics.mean(hourly_data[2880:3624]))
    monthly_Av.append(statistics.mean(hourly_data[3624:4344]))
    monthly_Av.append(statistics.mean(hourly_data[4344:5088]))
    monthly_Av.append(statistics.mean(hourly_data[5088:5832]))
    monthly_Av.append(statistics.mean(hourly_data[5832:6552]))
    monthly_Av.append(statistics.mean(hourly_data[6552:7296]))
    monthly_Av.append(statistics.mean(hourly_data[7296:8016]))
    monthly_Av.append(statistics.mean(hourly_data[8016:8760]))
    
    return monthly_Av

def average_scaled_monthly(hourly_data):
    m = average_monthly(hourly_data)
    max_output = max(hourly_data) 
    scaled_monthly_Av = [x/max_output for x in m]
    return scaled_monthly_Av

def average_daily(hourly_data):
    daily_Av = []
    daily_data = []
    for row, val in enumerate(hourly_data):
        daily_data.append(hourly_data[row])    
        if len(daily_data) == 24:
            daily_Av.append((sum(daily_data)/len(daily_data)))
            daily_data.clear()        
    return daily_Av

def average_scaled_daily(hourly_data):
    d = average_daily(hourly_data)         
    max_output = max(hourly_data) 
    scaled_daily_Av = [x/max_output for x in d]        
    return scaled_daily_Av
    

Syn_Monthly_Average = average_monthly(Syn_Out_Hourly)
Kil_Monthly_Average = average_monthly(Kil_Out_Hourly)
Bea_Monthly_Average = average_monthly(Bea_Out_Hourly)

Syn_Scaled_Monthly_Average = average_scaled_monthly(Syn_Out_Hourly)
Kil_Scaled_Monthly_Average = average_scaled_monthly(Kil_Out_Hourly)
Bea_Scaled_Monthly_Average = average_scaled_monthly(Bea_Out_Hourly)
Sum_Scaled_Monthly_Average = (np.array(Syn_Scaled_Monthly_Average)+np.array(Kil_Scaled_Monthly_Average)+np.array(Bea_Scaled_Monthly_Average))/3

Syn_Daily_Average = average_daily(Syn_Out_Hourly)
Kil_Daily_Average = average_daily(Kil_Out_Hourly)
Bea_Daily_Average = average_daily(Bea_Out_Hourly)

Syn_Scaled_Daily_Average = average_scaled_daily(Syn_Out_Hourly)
Kil_Scaled_Daily_Average = average_scaled_daily(Kil_Out_Hourly)
Bea_Scaled_Daily_Average = average_scaled_daily(Bea_Out_Hourly)
Sum_Scaled_Daily_Average = (np.array(Syn_Scaled_Daily_Average)+np.array(Kil_Scaled_Daily_Average)+np.array(Bea_Scaled_Daily_Average))/3

# plt.figure(1)
# #plt.plot(Months,Syn_Monthly_Average,Months,Kil_Monthly_Average,Months,Bea_Monthly_Average)
# fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
# ax1.plot(Months, Syn_Monthly_Average)
# ax2.plot(Months, Kil_Monthly_Average)
# ax3.plot(Months, Bea_Monthly_Average)
# ax1.set_ylim([min(Syn_Monthly_Average), max(Syn_Monthly_Average)])
# ax2.set_ylim([min(Kil_Monthly_Average), max(Kil_Monthly_Average)])
# ax3.set_ylim([min(Bea_Monthly_Average), max(Bea_Monthly_Average)])
# ax1.set_title('Monthly Average of Synthesised Windfarm')
# ax2.set_title('Monthly Average of Curtailed Output of Kilbraur')
# ax3.set_title('Monthly Average of Metered Output of Beatrice')
# ax1.grid(b=True, which='major', color='#cccac6', linestyle='-')
# ax2.grid(b=True, which='major', color='#cccac6', linestyle='-')
# ax3.grid(b=True, which='major', color='#cccac6', linestyle='-')
# fig1.tight_layout()

# date_stamp = []
# for row, val in enumerate(date_time_stamp):
#     if row % 24 == 0:
#         date_stamp.append(date_time_stamp[row][0:10])

# plt.figure(2)        
# #plt.plot(date_stamp,Syn_Daily_Average,date_stamp,Kil_Daily_Average,date_stamp,Bea_Daily_Average)
# fig2, (ax4, ax5, ax6) = plt.subplots(3, 1, sharex=True)
# ax4.plot(date_stamp, Syn_Daily_Average)
# ax5.plot(date_stamp, Kil_Daily_Average)
# ax6.plot(date_stamp, Bea_Daily_Average)
# ax4.set_ylim([min(Syn_Daily_Average), max(Syn_Daily_Average)])
# ax5.set_ylim([min(Kil_Daily_Average), max(Kil_Daily_Average)])
# ax6.set_ylim([min(Bea_Daily_Average), max(Bea_Daily_Average)])
# ax4.set_title('Daily Average of Synthesised Windfarm')
# ax5.set_title('Daily Average of Curtailed Output of Kilbraur')
# ax6.set_title('Daily Average of Metered Output of Beatrice')
# ax4.grid(b=True, which='major', color='#cccac6', linestyle='-')
# ax5.grid(b=True, which='major', color='#cccac6', linestyle='-')
# ax6.grid(b=True, which='major', color='#cccac6', linestyle='-')
# fig2.tight_layout()
        
    



      
       