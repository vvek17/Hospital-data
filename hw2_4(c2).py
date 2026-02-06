import pandas as pd

# 1. Load the categorized dataset
df = pd.read_csv("gymX_categorized.csv", encoding='ISO-8859-1')

# 2. Ensure 'sex' column contains strings 'male' and 'female'
df['sex'] = df['sex'].replace({1: 'male', 0: 'female'})

# 3. Define the lists for looping
genders = ['female', 'male']
categories = ['kids', 'youth', 'adults']

print("--- Group-wise Mean Calculations ---\n")

# 4. Nested loop to process all 6 combinations
for s in genders:
    for cat in categories:
        # Create a filter condition for the current gender and category
        filter_condition = (df['sex'] == s) & (df['membership_type'] == cat)
        
        # Isolate the data for this specific group
        group_df = df[filter_condition]
        
        # Calculate the mean values (missing values are ignored automatically)
        h_mean = group_df['height'].mean()
        w_mean = group_df['weight'].mean()
        
        # Round the values for cleaner display and imputation
        h_mean_round = round(h_mean) if pd.notnull(h_mean) else 0
        w_mean_round = round(w_mean) if pd.notnull(w_mean) else 0
        
        # Print results with proper labels
        print(f"Gender: {s.capitalize()} | Category: {cat.capitalize()}")
        print(f"  -> Average Height: {h_mean_round}")
        print(f"  -> Average Weight: {w_mean_round}")
        print("-" * 30)
        
        # 5. Fill the missing values in the original dataframe for this specific group
        df.loc[filter_condition, 'height'] = df.loc[filter_condition, 'height'].fillna(h_mean_round)
        df.loc[filter_condition, 'weight'] = df.loc[filter_condition, 'weight'].fillna(w_mean_round)

# 6. Save the final cleaned data
df.to_csv("gymX_final_cleaned.csv", index=False)
print("\nSuccess! All 6 groups processed and saved to 'gymX_final_cleaned.csv'.")

# Filter only kids
kids_df = df[df['membership_type'] == 'kids']

