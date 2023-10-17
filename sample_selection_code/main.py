import random 
import pandas as pd

df = pd.read_csv('sample_data.csv')

#create new dataframe with columns "LabID" and "IndividualID":
df1  = df[["LabID","IndividualID"]]

#print(df1.head(10))

LabID = df["LabID"].tolist()
coyoteID = df["IndividualID"].tolist()
isEqualLength = len(LabID) == len(coyoteID)

#print(isEqualLength)

numSamples = len(LabID) 
coyotes = {}

for i in range(numSamples):
    if pd.isna(coyoteID[i]) or "dog" in coyoteID[i] or "RF" in coyoteID[i]:
        continue

    if coyoteID[i] in coyotes.keys():
        coyotes[coyoteID[i]].append(LabID[i])
    else:
        coyotes[coyoteID[i]] = list([LabID[i]])


numberToDelete = (len(coyotes.keys()) - 50) if len(coyotes.keys()) > 50 else 0

for i in range(numberToDelete):
    keyToDelete = random.choice(list(coyotes.keys()))
    del coyotes[keyToDelete]

#print(len(coyotes.keys()))

# for key in coyotes.keys():
#    print(f"{key}: {coyotes[key]}")

selectedCoyotes = []
selectedSamples = []

for key in coyotes.keys():
    selectedCoyotes.append(key)
    selectedSamples.append(random.choice(coyotes[key]))

df2 = pd.DataFrame({"CoyoteID" : selectedCoyotes, 
                   "LabID" : selectedSamples})

df3 = pd.DataFrame({"LabID" : selectedSamples})

#print(df2)

df2.to_csv('SelectedCoyotesAndSamples.csv', index=False)

df3.to_csv('SelectedSamples.csv', index=False)

print("Script ran successfullllyy!")

