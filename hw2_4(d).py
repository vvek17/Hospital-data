import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


df_naive = pd.read_csv("gymX_naive.csv")
df_better = pd.read_csv("gymX_final_cleaned.csv") # ફાઈલનું નામ ચેક કરી લેજો

plt.figure(figsize=(12, 6))

# Plot Naive
plt.subplot(1, 2, 1)
sns.histplot(df_naive['weight'], kde=True, color='red')
plt.title(f"Naïve Imputation\nMean: {df_naive['weight'].mean():.2f} | Std: {df_naive['weight'].std():.2f}")

# Plot Better
plt.subplot(1, 2, 2)
sns.histplot(df_better['weight'], kde=True, color='green')
plt.title(f"Group-wise Imputation\nMean: {df_better['weight'].mean():.2f} | Std: {df_better['weight'].std():.2f}")

plt.tight_layout()

# plt.show() 
plt.savefig("comparison_plot.png") 
print("Graph saved as 'comparison_plot.png'. Check your folder!")