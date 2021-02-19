# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:36:36 2020

@author: Fin Christie
"""

import pandas as pd

df =  pd.read_csv (r"C:\Users\Fin Christie\Documents\Uni\4th Year\EM401\Data\Data from Graeme's Sharefile\2019\BAVs.csv")
df_list = df['T_KILBW-1'].tolist()
aggregated_data = []
hourly_data = []

for row, val in enumerate(df_list):
    hourly_data.append(df_list[row])
    
    if len(hourly_data) == 2:
        aggregated_data.append((sum(hourly_data)*1000))
        hourly_data.clear()
        
        
      
       