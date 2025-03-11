import pandas as pd
import random

# Load the updated CSV file
#df_customer = pd.read_csv('datasets/onlinefood_with_customer_id.csv')

# Define the list of fast food options
#fast_food_options = ["KFC", "McDonald's", "Burger King", "Wendy's", "Taco Bell", "Pizza Hut"]

# Add the favorite_fastfood column with random values
#df_customer['favorite_fastfood'] = [random.choice(fast_food_options) for _ in range(len(df_customer))]

# Save the updated CSV file
#df_customer.to_csv('datasets/onlinefood_with_#customer_id.csv', index=False)

#print("favorite_fastfood column added successfully.")

# Load the FastFoodNutritionMenuV2 CSV file
df_fastfood = pd.read_csv('datasets/FastFoodNutritionMenuV2.csv')
df_customer = pd.read_csv('datasets/onlinefood_with_customer_id.csv')

#mette _ negli spazi nei nomi delle colonne
df_customer.columns = df_customer.columns.str.replace(" ", "_")

# Perform the join between the two DataFrames
df_merged = pd.merge(df_customer, df_fastfood, left_on='favorite_fastfood', right_on='Company', how='inner')

# Save the merged DataFrame to a new CSV file
df_merged.to_csv('datasets/merged_customer_fastfood.csv', index=False)

print("DataFrames merged and saved successfully.")