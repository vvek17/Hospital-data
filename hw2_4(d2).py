import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset you cleaned earlier
df = pd.read_csv("gymX_final_cleaned.csv")

# 2. Set the size of the graph window
plt.figure(figsize=(10, 6))

# 3. Create a Bar Plot (Count Plot)
# 'x' is the membership category (Kids, Youth, Adults)
# 'hue' splits each category into Male and Female bars
# 'palette' sets the colors of the bars
sns.countplot(
    data=df, 
    x='membership_type', 
    hue='sex', 
    palette='viridis', 
    order=['kids', 'youth', 'adults']
)

# 4. Add a Title and Labels for the X and Y axes
plt.title('Total Customers by Sex and Membership Type', fontsize=15)
plt.xlabel('Membership Category', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)

# 5. Add a Legend to explain the colors (Male vs Female)
plt.legend(title='Sex')

# 6. Save the graph as an image file
# This is better than plt.show() because it won't freeze your computer
plt.savefig("customer_count_barplot.png")

# 7. Print a message so you know it finished
print("Success! The bar plot has been saved as 'customer_count_barplot.png'.")