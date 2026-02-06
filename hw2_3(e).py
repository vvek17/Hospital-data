import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("heart_disease_full.csv")

#  Box Plot 
plt.figure(figsize=(6, 4))
sns.boxplot(x='sex', y='num', data=df)

#title and labels
plt.title('Sex vs Num')
plt.show()

# Analysis: 0 = FEMALE , 1 = MALE 
# From the box plot, we can observe that 0 (female) have a lower heart dsease severity (num) compared to 1 (male).
# Female patients tend to have lower median num values, indicating less severe heart disease cases on average.
# I guess as per the box plan sex does have an impact on heart disease severity..