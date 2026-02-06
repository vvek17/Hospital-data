import pandas as pd
import numpy as np

#b Describe a naive solution for missing values and use it to solve the missing data problem.
   #What are the advantages/disadvantages of this solution?

#Naive solution: 

#A naive solution for missing data refers to simple, straightforward, and often unoptimized techniques that address missingness without considering the underlying data distribution or structure. These methods are quick and easy to implement but often introduce bias, underestimate variance, or lose significant information. 

#Listwise Deletion (Complete Case Analysis): Removing entire records (rows) that contain any missing values.
#Mean/Median/Mode Imputation: Replacing missing numerical values with the mean or median, and categorical values with the mode of that column.
#Dropping Columns: Deleting entire columns (features) if they contain a high percentage of missing values.
#Last Observation Carried Forward (LOCF): Used in time-series data, this method replaces a missing value with the last known value from the same subject.
# Ignoring the Issue: In some algorithms, like Naive Bayes, missing values can simply be skipped during calculations. 

#here we have missing value for height, weight and membership_type. so for that we will use mean and mode to fill up that place and get the new csv file as a output

#get hte dataset with the header with skipping 0 row, I did search up again from this video(https://www.youtube.com/watch?v=lc6YIfHUF-I) i got to know we can put header as whichever we want to read. 
df = pd.read_csv("hw2_GymX(1).csv", encoding='ISO-8859-1', header=1)

#finding mean value for weight and height
weight_mean = df['weight'].mean()
height_mean = df['height'].mean()

#finding mode for membership_type
membership_mode = df['membership_type'].mode()[0]
print(f"Mode value of 'membership_type' column: {membership_mode}")
#round up

weight_round = int(round(weight_mean))
height_round = int(round(height_mean))

#fill up the missing value with mean and mode

df['weight'] = df['weight'].fillna(weight_round)
df['height'] = df['height'].fillna(height_round)
df['membership_type'] = df['membership_type'].fillna(membership_mode)

# new csv file after cleaning
df.to_csv("gymX_naive.csv", index=False)



# I believe naive solution is not good for this dataset as mean imputation reduces variance and ignores relationships between variables. Also, if the data is not missing completely at random, it can introduce bias. For categorical data. For this dataset 4705,Danny Montero,9,1,4.5,69.0,kids is there, so mean imputation for height and weight may not be appropriate as a 9-year-old's measurements will differ significantly from adults.