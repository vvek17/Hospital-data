# as per given given csv file and given instruction change the datatype of perticular thing
import pandas as pd
import statistics as stats

df = pd.read_csv("heart_disease_full.csv")

#age in integer
df['age'] = df['age'].astype(int)

#convert sex into boolean 1:male 2:female
df['sex'] = df['sex'].replace({1 : 'male', 0 : 'female'})

#cp conversion
df['cp'] = df['cp'].replace({
    1: 'Typical Angina',
    2: 'Atypical Angina',
    3: 'Non-anginal Pain',
    4: 'Asymptomatic'
})

#fasting blood suger
df['fbs'] = df['fbs'].replace({1: 'True(>120 mg/dl)', 0: 'False'})

#restingECG
df['restecg'] = df ['restecg'].replace( {
    0:'normal',
    1:'ST-T Wave Abnormality',
    2:'Left Ventricular Hypertrophy' 
})

#exercise include angine
df['exang'] = df['exang'].replace({
    1: 'Yes',
    0: 'no'
})

#slope of ST segment
df['slope'] = df['slope'].replace({
    1: 'Upsloping',
    2: 'Flat',
    3: 'Downsloping'
})
#Thal
df['thal'] = df['thal'].replace({
    3: 'Normal',
    6: 'Fixed Defect',
    7: 'Reversable Defect'
})

#print head
print(df.head())

#a : The associated task with this dataset is multiclass classification. Change the problem to binary classification and compute the proportion of each class in the binary case? Is this a balanced dataset?

# it says it just need multiclass Binary classification means num column into 0 and 1

#converting num into binary to get result
df['num'] = df['num'].replace({
        0: 0,   
        1: 1,
        2: 1,
        3: 1,
        4: 1
    })

# now convert num column values into percentage for 1 and rest of them 0

total_patients = len(df)
disease_patients = len(df[df['num'] == 1])
no_disease_patients = len(df[df['num'] == 0])   

disease_percentage = (disease_patients / total_patients) * 100
no_disease_percentage = (no_disease_patients / total_patients) * 100    

print(f"Percentage of patients with heart disease: {disease_percentage:.2f}%")
print(f"Percentage of patients without heart disease: {no_disease_percentage:.2f}%")

# checking balanced dataset or not
#here Percentage of patients with heart disease: 45.87%
#Percentage of patients without heart disease: 54.13% 

#as we can see its nearly 50-50 so its balanced dataset

#b: Remove all patients who have any missing values in their records. How many patients do you have now?

#checking missing values 
missing_values_count = df.isnull().sum().sum() 
#1st sum() is for finding all 0 in each column and 2nd sum() is for adding all those values 
print(f"Total missing values in the dataset: {missing_values_count}")
# Remove rows with any missing values
df_cleaned = df.dropna()
print(f"Number of patients after removing missing values: {len(df_cleaned)}")

df_cleaned.to_csv("heart_disease_cleaned.csv", index=False)





