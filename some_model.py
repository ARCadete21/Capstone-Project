import pandas as pd
import numpy as np


########### IMPORT DATA ##############

data = pd.read_csv('data/data2022_2023.csv').drop(['Unnamed: 0', 'country'], axis=1)

data.info()
data.head().T
######### EDA #################

race_df = data[["year", "round", "circuitRef"]].copy()


