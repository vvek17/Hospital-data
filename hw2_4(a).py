import pandas as pd
import numpy as np

df_excel = pd.read_excel("hw2_GymX(1).xlsx")

#convert to csv
df_csv = df_excel.to_csv("hw2_GymX(1).csv", index=False)

df = pd.read_csv("hw2_GymX(1).csv")

#a Report the number of missing values in each feature
#subset_df = df.iloc[:, 1:7]  # Select columns from index 1 to 6
#missing_counts = subset_df.isnull().sum()

#for col_name, count in missing_counts.items():
 #   print(f"{col_name}: {count} missing values")

# from this code i got output as :
# Unnamed: 1: 0 missing values
# Unnamed: 2: 0 missing values
# Unnamed: 3: 0 missing values
# Unnamed: 4: 2976 missing values
# Unnamed: 5: 2817 missing values
# Unnamed: 6: 1455 missing values

# so now i am going to change name of the columns for better understanding
df = df.rename(columns={
    'Unnamed: 1': 'customer_name',
    'Unnamed: 2': 'age',
    'Unnamed: 3': 'sex',                
    'Unnamed: 4': 'height',
    'Unnamed: 5': 'weight',
    'Unnamed: 6': 'membership_type'
})

#giving new name for this renames

new_column_names = ["customer_name", "age", "sex", "height", "weight", "membership_type"]
subset_df = df[new_column_names]

#find missing value
missing_count = subset_df.isnull().sum()
for col_name, count in missing_count.items():
    print(f"{col_name}: {count} missing values")