#) Propose a better solution and use it to solve the missing data problem

# for the better solution, firstly I am going to take age coloum and use if else method with the distribution of ages and bu the group of ages put kids, youth and adults
# "Group-wise Imputation"

import pandas as pd
import numpy as np      

df = pd.read_csv("hw2_GymX(1).csv", encoding='ISO-8859-1', header=1)

#function to categorize age

def define_membership(age):
    if 1 <= age <= 12:
        return "kids"
    elif 13 <= age <= 17:
        return "youth"
    else:
        return "adults"
    
# applying this age categorization to membership_type coluxmn

df['membership_type'] = df['age'].apply(define_membership)

#download it into new csv file
df.to_csv("gymX_categorized.csv", index=False)
