# Green_Hydrogen_Production_Project

## Aims and Objectives of Project
- The aim of this project is to review Green Hydrogen’s prospects for becoming a significant part of the UK’s energy sector, by assessing what it can offer and the barriers that it faces. while evaluating its optimal configuration for the UK’s existing electricity and gas grid by creating a multi-energy system model using Calliope software.

- The project will focus specifically on Green Hydrogen, produced using electrolysis, using electricity obtained from offshore wind (OSW) sources in Scotland. This scenario is best suited to the UK government’s recent climate plan and is in line with the Climate Change Committee’s Sixth Carbon Budget [1].

- Several Hydrogen production scenarios will be simulated using a multi-energy system modelling software (Calliope) a comparison will be drawn between the scenarios to find which are the most cost effective – considering both monetary and carbon cost.

- Each scenario will also be optimised using Calliope’s planning mode, which can be used to assess the optimum capacity of offshore wind (OSW) and electrolyser - between a set of defined constraints - during a simulation

## Model Key Input Parameters
- CAPEX and O&M Costs of green hydrogen production system components (£/kW) in 2030
- Wholesale Cost of electricity (£/kWh)
- LCOE of Blue Hydrogen (£/kWh)
- Expected emissions and carbon prices of non-zero carbon industries (£/kgCO2)
- Time-variant OSW resource (kWh)
- Time-variant electricity demand (kWh)
- Fixed hydrogen demand (kWh)
- Level of subsidy for Green Hydrogen (£/kWh) (will be varied)

## Model Decision Variables
- Installed Electrolyser capacity (kW)
- Installed Battery Capacity (kW)
- Energy vector flow throughout entire system.

- Model can be set to find the optimal value for each of these variables, the choice of decision variables may change for different scenarios/ runs

## Model Objective
- Minimise costs, while ensuring both electricity and hydrogen demands are met

## Model Key Output Parameters
- Optimal Capacities of green hydrogen production system components (kW)
- Capacity factors of green hydrogen production system components (%)
- Total cost of each green hydrogen production system components (£)
- LCOE of green hydrogen production (may include both hydrogen and electricity production) (£/kWh)
- Minimum level of subsidy required for green hydrogen production to be cost competitive (run the model multiple times with varying levels of hydrogen subsidy) (£/kWh)


## Model Testing Procedure
- The model testing procedure is yet to be fully established, however a basic outline is known at this stage
- The main methods of testing the model’s outputs to test are:
  - Ensuring sensibility: this can be done by analysing the data and using the concept of validation: comparing the quantitative outputs of the simulation to external data.    For example comparing the windfarm and electrolyser capacity factors against published real-word statistics.
  - Ensuring feasibility: Calliope can do this automatically using a run configuration setting “ensure_feasibility”. This means that unmet demand becomes a decision variable to account for an ability to meet demand with an available supply
  - Ensuring outputs are affected by constraints: This would involve a simple test to ensure that when a constraint is applied to the model, this change is reflected in the simulation’s output

## Concept Scenario 1
- A hypothetical OSW farm directly connected onshore electrolyser.
- Energy can be stored in a battery, used to produce hydrogen or exported to the electricity grid. 
- In this scenario the system includes an OSW farm, a battery and an electrolyser, the capital and operational and maintenance cost of all three system components will be considered within the model.


## Concept Scenario 2
- A hypothetical OSW farm directly connected to an offshore electrolyser (platform).
- Energy can be stored in an offshore battery or converted to hydrogen. Energy can only be transported to shore in the form of hydrogen.
- This scenario contains the same system components as Concept Scenario 1, however as the electrolyser and battery are now situated offshore they will have different associated costs.
- Additionally, hydrogen pipes will be used in place of undersea HVAC cables, this change will be represented by the costs of the OSW farm and electrolyser. 


## Concept Scenario 3
- An onshore electrolyser directly connected to Beatrice windfarm.
- Like Concept Scenario 1, energy can be stored in a battery, used to produce hydrogen or exported to the electricity grid.
- In this scenario the system does not include the OSW farm; its output is simply an input to the system.
- Therefore, the CAPEX and OPEX of the windfarm is not included, however there is a cost per unit of energy associated with the system’s consumption of OSW electricity.


## Concept Scenario 4
- An onshore electrolyser that only has access to the curtailed energy of Kilbraur (onshore) windfarm.
- Kilbraur was used as a proxy for Beatrice windfarm because Beatrice very rarely curtails its output and looks to sell at an exceptionally low price to avoid doing so. Kilbraur is an onshore windfarm but is located in the North East of Scotland and experiences similar levels of wind energy density.
- Like in Concept Scenario 3, only the CAPEX and OPEX of the electrolyser and battery is considered, however there is no cost associated with the curtailed energy.

## Run Scripts
Contains jupyter note books that are used to run the model multiple times.
 - Run Attempts: used for testing code and functions
 - Green Hydrogen Production Model: Contains full working script for running Calliope model multiple times. The script uses funcions to save the results of each run to a specfic file in Results_Files


