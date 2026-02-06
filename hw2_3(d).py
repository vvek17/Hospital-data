#2(D) Draw a scatter plot and explain the relationship between chest pain type and age?


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(10, 6))

df = pd.read_csv("heart_disease_full.csv")
x = df['age']
y = df['cp']

plt.scatter(x, y)

plt.xlabel("Age")
plt.ylabel("Chest Pain Type")
plt.title("Relationship Between Age and Chest Pain Type")

plt.show()

# Analysis:
# From the scatter plot, we can observe the distribution of chest pain types across different ages. 
# It appears that age 40 to 60  have majorly 3.0 = non-anginal pain and 4.0 =  asymptomatic pain 
# For example, younger individuals tend to report 'Typical Angina'(value 1) more frequently,             

