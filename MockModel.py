# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:06:54 2020

@author: Fin Christie
"""

"""
Basic Proof of Concept OSW/Electrolysis Energy Model

Assumptions:
    1. OSW is variably capable of supplying the entirety of the UK's energy demand
    2. OSW electricity supply is sometimes above national demand and sometimes below national demand
    3. OSW is considered as one single centralised energy source (one large windfarm)
    4. Hydrogen produced by electrolysis is done so at a constant efficiency i.e. 
    
"""

"""
Inputs to Model:

    1. OSW Electricity supply
    2. National Electricity Demand Data
    3. Kg of H2 per KWh
    
Outputs of model:
    
    1. Total cumulative Hydrogen production 
    2. Combined output of OSW and Hydrogen

"""

import pandas as pd
import numpy as np

demand_data = pd.read_csv (r'C:/Users/Fin Christie/Documents/Uni/4th Year/EM401/Data/2019\Gridwatch.csv')
demand_data_hrly = np.array(demand_data[0::12])


