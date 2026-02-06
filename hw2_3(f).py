import pandas as pd

df = pd.read_csv("heart_disease_cleaned.csv")
for i in range(1,7):
    
    #  Create a random sample of 50 patients from the dataset and here we will take random_state = i for different samples as it cannot be same every time. 
    random_sample = df.sample(n=50, replace=False, random_state=i)

#make it binary so beside 0 every number =1 
    random_sample['num'] = random_sample['num'].replace({
        0: 0,   
        1: 1,
        2: 1,
        3: 1,
        4: 1
    })

# 1 = heart attack patient
    count = len(random_sample[random_sample['num'] == 1])
    percentage = (count / 50) * 100
    print(f"Percentage of patients: {percentage:.2f}%")

#2 = not heart attack patient
    count_2 = len(random_sample[random_sample['num'] == 0])
    percentage_2 = (count_2 / 50) * 100
    print(f"Percentage of patients without heart disease: {percentage_2:.2f}%")

#analysis: I chose random_state = 1 cause I thought this will be good for loop. but it was giving me same answer so then I put my code in LLM and it suggested me to use i in random_state so that every time it will give different sample.
#as we can see percentage of heart disease patient is varying every time as sample is changing every time.
#as out of 6 samples 5 times percentage of patients without heart attack is between 40-60% so I can say its likely that in random sample of 50 patients this dataset will give balanced result.


import matplotlib.pyplot as plt
import seaborn as sns
# Create a sample DataFrame
plt.figure(figsize=(6, 4))
sns.boxplot(x='sex', y='num', data= random_sample)

#title and labels

plt.title(f'sample {i}: Sex vs Num')
plt.show()
