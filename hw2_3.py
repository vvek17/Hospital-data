from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata 
print(heart_disease.metadata) 
  
# variable information 
print(heart_disease.variables) 

# view data
df = pd.concat([X, y], axis=1)

print(df.head())
print(df.info())

#whole dataset in excel


df.to_csv("heart_disease_full.csv", index=False)
print("File 'heart_disease_full.csv' created! Open this in Excel to see everything.")

