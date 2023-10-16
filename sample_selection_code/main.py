import random 
import pandas as pd

df = pd.read_csv('sample_data.csv')

#create new dataframe with columns "LabID" and "IndividualID":
df1  = df[["LabID","IndividualID"]]

#print(df1.head(10))

LabID = df["LabID"].tolist()
coyoteID = df["IndividualID"].tolist()
isEqualLength = len(LabID) == len(coyoteID)

print(isEqualLength)

numSamples = len(LabID) 
coyotes = {}

for i in range(numSamples):
    if pd.isna(coyoteID[i]):
        continue

    if coyoteID[i] in coyotes.keys():
        coyotes[coyoteID[i]].append(LabID[i])
    else:
        coyotes[coyoteID[i]] = list([LabID[i]])

#for key in coyotes.keys():
    #print(f"{key}: {coyotes[key]}")

numberToDelete = len(coyotes.keys()) - 50

print(numberToDelete)


