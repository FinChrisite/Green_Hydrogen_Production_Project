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

## Model Testing Procedure
- The model testing procedure is yet to be fully established, however a basic outline is known at this stage
- The main methods of testing the model’s outputs to test are:
  - Ensuring sensibility: this can be done by analysing the data and using the concept of validation: comparing the quantitative outputs of the simulation to external data.    For example comparing the windfarm and electrolyser capacity factors against published real-word statistics.
  - Ensuring feasibility: Calliope can do this automatically using a run configuration setting “ensure_feasibility”. This means that unmet demand becomes a decision variable to account for an ability to meet demand with an available supply
  - Ensuring outputs are affected by constraints: This would involve a simple test to ensure that when a constraint is applied to the model, this change is reflected in the simulation’s output

## Concept Scenario 1
- Dedicated (small) windfarm for onshore electrolyser
  - Electrolyser around 80% of OSW capacity, model will be run in planning mode to see if this is optimal capacity
- When there is surplus OSW output it is sent to national electricity grid
- When there is not enough OSW output, less hydrogen is produced
- On site hydrogen and electricity storage capabilities

## Concept Scenario 2
- Dedicated (small) windfarm for offshore electrolyser (on platforms)
  - Electrolyser around 100 % of OSW capacity
- Model will find if this is optimal capacity
- If there happens to be surplus OSW output, on-platform batteries will be used
- Hydrogen will be transported to shore using underwater pipes
- Electricity will not be transported to shore

## Concept Scenario 3
- Electrolysis facility is integrated into a much larger windfarm, the primary purpose of which is to produce electricity for grid users.
- Electrolysers are connected on the OSW side of grid to ensure lower transmission charges
- Electrolysers are considered as just another grid user, in that they have a set demand
- The optimal electrolyser capacity/ demand will be found by the model using the planning mode

## Concept Scenario 4
- Similarly, electrolysis facility is integrated into a much larger windfarm, the primary purpose of which is to produce electricity for grid users.
- Electrolysers are connected on the OSW side of grid to ensure lower transmission charges
- Electrolysers only make use of OSW electricity that would otherwise be curtailed
- This concept may offer a solution to the variability of supply issue for OSW
- The optimal electrolyser capacity/ demand will be found by the model using the planning mode



