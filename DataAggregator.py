# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:36:36 2020

@author: Fin Christie
"""

import pandas as pd
import numpy as np

df =  pd.read_csv (r'C:/SPB_Data/EM401_Code/Green_Hydrogen_Production_Project/ff_Model_v0.6.6/timeseries_data/Beatrice_raw_output_hourly.csv')
df_list = df["region1-1"].tolist()
aggregated_data = []
hourly_data = []

df_arr = np.array(df_list)
df_arr[np.isnan(df_arr)] = 0
df_list = df_arr.tolist()


for row, val in enumerate(df_list):
    hourly_data.append(df_list[row])
    
    if len(hourly_data) == 24:
        aggregated_data.append((sum(hourly_data)))
        hourly_data.clear()
        
        
      
       