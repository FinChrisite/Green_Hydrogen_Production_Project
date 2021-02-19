# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:36:36 2020

@author: Fin Christie
"""

import pandas as pd

df =  pd.read_csv (r'C:\Users\Fin Christie\Documents\Uni\4th Year\EM401\Data\Windfarm_Data_Analysis.csv')
df_list = df["Beatrice"].tolist()
aggregated_data = []
hourly_data = []

for row, val in enumerate(df_list):
    hourly_data.append(df_list[row])
    
    if len(hourly_data) == 672:
        aggregated_data.append((sum(hourly_data)/672))
        hourly_data.clear()
        
        
      
       