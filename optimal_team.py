import pandas as pd
import numpy as np
import ast

# attempt to get the cost and points from the fantasy
'''dr_data = pd.read_csv('data/F1_23_drivers_basic.csv').drop(columns=['color', 'constructor'])
ct_data = pd.read_csv('data/F1_23_constructors_basic.csv').drop(columns=['color', 'constructor'])

verstapen_results = ast.literal_eval(dr_data.race_results[0])

# Normalize the nested dictionaries into columns
df = pd.json_normalize(verstapen_results)

df = df.loc[:,['id', 'results_per_aggregation_list','results_per_race_list']]

df.iloc[:,-1][:2]



for driver_index in dr_data:
    
    driver_results = ast.literal_eval(dr_data.race_results[driver_index])
    
    create_df = pd.json_normalize(driver_results)
    
    create_df = create_df.loc[:,['id', 'results_per_aggregation_list','results_per_race_list']]
    
    print(create_df.iloc[:,-1][:2])'''

















# first value is the cost to select in the fantasy
# and its followed by the avg points made during the season
drivers = {'verstappen': [30, 20],
           'perez': [20, 18],
           
           'hamilton': [25, 16],
           'russell': [20, 17],
           
           'leclerc': [25, 19],
           'sainz': [20, 15],
           
           'alonso': [12, 12],
           'stroll': [8, 8],
           
           'norris': [15, 14],
           'piastri': [8, 2],
           
           'ocon': [9, 13],
           'gasly': [8, 9],
           
           'de_vries': [5, 4],
           'tsunoda': [5, 7],
           
           'bottas': [8, 11],
           'zhou': [6, 6],
           
           'albon': [5, 5],
           'sargeant': [4, 1],
           
           'magnussen': [6, 10],
           'hulkenberg': [5, 3],
           }

# first value is the cost to select in the fantasy
# and its followed by the avg points made during the season
constructors = {'red_bull': [30, 10],
                'mercedes': [25, 8],
                'ferrari': [25, 9],
                'aston_martin': [8, 4],
                'mclaren': [12, 6],
                'alpine': [10, 7],
                'alpha_tauri': [5, 2],
                'williams': [4, 1],
                'alfa_romeo': [6, 5],
                'haas': [6, 3],
                }


from itertools import combinations

def optimize_team(drivers, constructors, max_capacity):
    best_value = 0
    best_team = None

    # Generate combinations of 5 drivers
    driver_combinations = combinations(drivers.keys(), 5)

    # Iterate through all combinations
    for drivers_combo in driver_combinations:
        # Generate combinations of 2 constructors for each driver combination iteration
        constructor_combinations = combinations(constructors.keys(), 2)

        for constructors_combo in constructor_combinations:
            # Calculate total weight and value for the combination
            total_weight = sum(drivers[driver][0] for driver in drivers_combo) + sum(constructors[constructor][0] for constructor in constructors_combo)
            total_value = sum(drivers[driver][1] for driver in drivers_combo) + sum(constructors[constructor][1] for constructor in constructors_combo)
            
            # Check if within weight limit and update best team
            if total_weight <= max_capacity and total_value > best_value:
                best_value = total_value
                best_team = (list(drivers_combo), list(constructors_combo))
    
    return best_value, best_team


# Usage
best_value, best_team = optimize_team(drivers, constructors, 100)
print("Best value:", best_value)
print("Best team (drivers, constructors):", best_team)
