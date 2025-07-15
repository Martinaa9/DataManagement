import pandas as pd

# Carica dimensioni
df_restaurant = pd.read_csv('datasets/restaurant_dimension.csv')
df_customer = pd.read_csv('datasets/customer_dimension.csv')
df_food = pd.read_csv('datasets/food_dimension.csv')

# Colonne finali della fact
final_cols = ['restaurant_key', 'customer_key', 'food_key', 'latitude', 'longitude', 'total_calories', 'total_protein', 'total_fat', 'total_carbs']

# Per restaurant_dimension
# Prendo solo le colonne di interesse se esistono, le altre metto NaN
df_rest = pd.DataFrame()
df_rest['restaurant_key'] = df_restaurant['restaurant_key']
df_rest['customer_key'] = pd.NA
df_rest['food_key'] = pd.NA
df_rest['latitude'] = df_restaurant['latitude'] if 'latitude' in df_restaurant.columns else pd.NA
df_rest['longitude'] = df_restaurant['longitude'] if 'longitude' in df_restaurant.columns else pd.NA
df_rest['total_calories'] = pd.NA
df_rest['total_protein'] = pd.NA
df_rest['total_fat'] = pd.NA
df_rest['total_carbs'] = pd.NA

# Per customer_dimension
df_cust = pd.DataFrame()
df_cust['restaurant_key'] = pd.NA
df_cust['customer_key'] = df_customer['customer_key']
df_cust['food_key'] = pd.NA
df_cust['latitude'] = df_customer['latitude'] if 'latitude' in df_customer.columns else pd.NA
df_cust['longitude'] = df_customer['longitude'] if 'longitude' in df_customer.columns else pd.NA
df_cust['total_calories'] = df_customer['total_calories'] if 'total_calories' in df_customer.columns else pd.NA
df_cust['total_protein'] = df_customer['total_protein'] if 'total_protein' in df_customer.columns else pd.NA
df_cust['total_fat'] = df_customer['total_fat'] if 'total_fat' in df_customer.columns else pd.NA
df_cust['total_carbs'] = df_customer['total_carbs'] if 'total_carbs' in df_customer.columns else pd.NA

# Per food_dimension
df_food_dim = pd.DataFrame()
df_food_dim['restaurant_key'] = pd.NA
df_food_dim['customer_key'] = pd.NA
df_food_dim['food_key'] = df_food['food_key']
df_food_dim['latitude'] = pd.NA
df_food_dim['longitude'] = pd.NA
df_food_dim['total_calories'] = df_food['total_calories'] if 'total_calories' in df_food.columns else pd.NA
df_food_dim['total_protein'] = df_food['total_protein'] if 'total_protein' in df_food.columns else pd.NA
df_food_dim['total_fat'] = df_food['total_fat'] if 'total_fat' in df_food.columns else pd.NA
df_food_dim['total_carbs'] = df_food['total_carbs'] if 'total_carbs' in df_food.columns else pd.NA

print("Righe restaurant:", len(df_restaurant))
print("Righe customer:", len(df_customer))
print("Righe food:", len(df_food))

# Unisci verticalmente tutti i dati
fact_nutrient_df = pd.concat([df_rest, df_cust, df_food_dim], ignore_index=True)

# Assicurati ordine colonne corretto
fact_nutrient_df = fact_nutrient_df[final_cols]

# Salva su CSV
fact_nutrient_df.to_csv('fact_nutrient.csv', index=False)

print("fact_nutrient.csv creato correttamente!")
