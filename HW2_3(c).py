import pandas as pd
import statistics as stats
df = pd.read_csv("heart_disease_full.csv")  


#as per describe I got value of mean for ca and thal coloumn 
ca_mean = df['ca'].mean()
thal_mean = df['thal'].mean()
print(f"Mean value of 'ca' column: {ca_mean}")
print(f"Mean value of 'thal' column: {thal_mean}")

#round the mean value # 0.67 -> 1   4.73 -> 5
ca_final = int(round(ca_mean))      
thal_final = int(round(thal_mean))  

print(f"Rounded CA: {ca_final}")
print(f"Rounded Thal: {thal_final}")

# 2. fillin missing values with mean
df['ca'] = df['ca'].fillna(ca_final)
df['thal'] = df['thal'].fillna(thal_final)

# 3. checking it 
print("Missing values filled successfully.")
print(df[['ca', 'thal']].head()) 

# new csv file after cleaning
df.to_csv("heart_disease_imputed_integer.csv", index=False)