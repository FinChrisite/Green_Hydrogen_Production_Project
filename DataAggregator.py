# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:36:36 2020

@author: Fin Christie
"""

import pandas as pd

df =  pd.read_csv (r'C:/SPB_Data/EM401_Code/Green_Hydrogen_Production_Project/ff_Model_v0.6.6/timeseries_data/Synth_1kW_osw_hourly.csv')
df_list = df["region1-1"].tolist()
aggregated_data = []
hourly_data = []

for row, val in enumerate(df_list):
    hourly_data.append(df_list[row])
    
    if len(hourly_data) == 24:
        aggregated_data.append((sum(hourly_data)))
        hourly_data.clear()
        
        
      
       