'''
Season data addition 
Carolyn Hanrahan + Sam Mason
March 19 2024 
The purpose of this script is to take season data (summer 2023 & fall 2022)
from our sample selection Excel file and append it to our metabarcoding results so that we have
corresponding season data linked with each sample in the same Excel file. 
'''

import pandas as pd

#dtype = {'LabID':str, 'IndividualID':str, 'YearCollected':str}

# Import data from CSV files (not xlsx)
df_selection = pd.read_csv('CoyoteMetabarcodingSelections_20231205.csv')


# print(df_selection)

# Creating lists by subsetting the selection dataframe to make 
# lists for LabID and Year (collected)
LabID = df_selection["LabID"].tolist()
Year = df_selection["YearCollected"].tolist()

print(len(LabID), len(Year))

# Populate a dictionary with LabID and Year lists
if len(LabID) == len(Year):
    num_selections = len(LabID)
else:
    print("THERE IS A PROBLEM")

season_samples = {}

for i in range(num_selections):
    season_samples[LabID[i]] = Year[i]

#print(season_samples)

# Import metabarcoding data CSV file:
df_results = pd.read_csv('Metabarcoding_clean_results.csv')

# for i in df_results.index:

print(df_results.keys())

# we have now extracted the keys from the results dataframe. Next, we pass
# these values into the dictonary to create a list of seasons. Then, append list to existing 
# df_results dataframe and save to csv. 

