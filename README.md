# Green_Hydrogen_Production_Project

## Aims and Objectives of Project
- The aim of this project is to review Green Hydrogen’s prospects for becoming a significant part of the UK’s energy sector, by assessing what it can offer and the barriers that it faces. while evaluating its optimal configuration for the UK’s existing electricity and gas grid by creating a multi-energy system model using Calliope software.

- The project will focus specifically on Green Hydrogen, produced using electrolysis, using electricity obtained from offshore wind (OSW) sources in Scotland. This scenario is best suited to the UK government’s recent climate plan and is in line with the Climate Change Committee’s Sixth Carbon Budget [1].

- Several Hydrogen production scenarios will be simulated using a multi-energy system modelling software (Calliope) a comparison will be drawn between the scenarios to find which are the most cost effective – considering both monetary and carbon cost.

- Each scenario will also be optimised using Calliope’s planning mode, which can be used to assess the optimum capacity of offshore wind (OSW) and electrolyser - between a set of defined constraints - during a simulation

## Model Decision Variables
- Problem is to decide what value each variable should take

- OSW Installed Capacity
- Electrolysis Capacity
- Transmission Capacities
- Energy Storage Capacity
- Rate of Hydrogen production

- Model can be set to find the optimal value for each of these variables, the choice of decision variables may change for different scenarios/ runs

## Model Constraints
- Constraints are able to either limit or fully define a variable

- Maximum Capacities for techs
- Minimum Capacities for techs
- Efficiency for techs
- Energy Carrier ratios (out/in)
- Resource
- Force resource (bool)

- These are just some of the possible constraints that can be used in Calliope, the full list can be found in software documentation

