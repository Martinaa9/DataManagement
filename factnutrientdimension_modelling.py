import pandas as pd

# 1. Caricamento dei primi 100 record di ogni dimensione
food_df = pd.read_csv('datasets/food_dimension.csv')
customer_df = pd.read_csv('datasets/customer_dimension.csv').head(25000)
restaurant_df = pd.read_csv('datasets/restaurant_dimension.csv')

# 2. Pulizia stringhe per evitare errori di matching
food_df['food_key'] = food_df['food_key'].str.strip().str.lower()
food_df['company'] = food_df['company'].str.strip().str.lower()

customer_df['item'] = customer_df['item'].str.strip().str.lower()
customer_df['company'] = customer_df['company'].str.strip().str.lower()

restaurant_df['name'] = restaurant_df['name'].str.strip().str.lower()

# 3. Join tra customer e food (match su item == food_key e company)
cf_df = pd.merge(
    customer_df, food_df,
    left_on=['item', 'company'],
    right_on=['food_key', 'company'],
    how='inner',
    suffixes=('_cust', '_food')
)

# 4. Join con restaurant (match su company == name)
cfr_df = pd.merge(
    cf_df, restaurant_df,
    left_on='company',
    right_on='name',
    how='inner'
)

# 5. Costruzione del factnutrient_dimension
factnutrient_df = cfr_df[[
    'restaurant_key',
    'customer_key',
    'food_key',
    'latitude_y',         # coordinate del ristorante
    'longitude_y',
    'total_calories_food',
    'total_protein_food',
    'total_fat_food',
    'total_carbs_food'
]].rename(columns={
    'latitude_y': 'latitude',
    'longitude_y': 'longitude',
    'total_calories_food': 'total_calories',
    'total_protein_food': 'total_protein',
    'total_fat_food': 'total_fat',
    'total_carbs_food': 'total_carbs'
})

# 6. Reset index (opzionale)
factnutrient_df = factnutrient_df.reset_index(drop=True)

# 7. Esportazione del risultato
factnutrient_df.to_csv('factnutrient_dimension.csv', index=False)

# 8. Visualizzazione delle prime righe
print(factnutrient_df.head())
