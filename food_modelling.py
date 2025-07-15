import pandas as pd

# Carica i due file CSV
df_food_clean = pd.read_csv('datasets/food_clean.csv')
df_fastfood_menu = pd.read_csv('datasets/FastFoodNutritionMenuV2.csv')

# Rinomina le colonne di FastFoodNutritionMenuV2 per farle combaciare
df_fastfood_menu = df_fastfood_menu.rename(columns={
    'Item': 'food_key',
    'Calories': 'total_calories',
    'Protein': 'total_protein',
    'Fat': 'total_fat',
    'Carbs': 'total_carbs',
    'Company': 'company'
})

# Aggiunge le colonne mancanti nel df_fastfood_menu
columns_to_add = ['ingredients', 'diet', 'flavor_profile', 'course', 'region']
for col in columns_to_add:
    df_fastfood_menu[col] = ''

# Ordina le colonne nello stesso ordine finale
final_columns = ['food_key', 'ingredients', 'diet', 'flavor_profile', 'course', 'region',
                 'total_calories', 'total_protein', 'total_fat', 'total_carbs', 'company']
df_fastfood_menu = df_fastfood_menu[final_columns]

# Rinomina la colonna 'name' in 'food_key' anche in df_food_clean
df_food_clean = df_food_clean.rename(columns={'name': 'food_key'})

# Aggiunge la colonna 'company' anche a df_food_clean con valore vuoto
df_food_clean['company'] = ''

# Ordina anche df_food_clean con le stesse colonne
df_food_clean = df_food_clean[final_columns]

# Concatena i due dataframe
df_food_dimension = pd.concat([df_food_clean, df_fastfood_menu], ignore_index=True)

# Metti tutte le prime lettere delle colonne in minuscolo
df_food_dimension.columns = [col.lower() for col in df_food_dimension.columns]

# Converte tutte le celle stringa in minuscolo
df_food_dimension = df_food_dimension.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# FUNZIONE OPZIONALE: FILTRO PER PRIMA PAROLA
def filter_by_first_word(df, key_col='food_key'):
    seen_first_words = set()
    selected_indices = []
    for idx, food_name in df[key_col].iteritems():
        first_word = food_name.split(' ')[0]
        if first_word not in seen_first_words:
            seen_first_words.add(first_word)
            selected_indices.append(idx)
    return df.loc[selected_indices]

#USO DEL FILTRO (decidere se usarlo o meno)
#df_food_dimension = filter_by_first_word(df_food_dimension, key_col='food_key')

# Rimuove i duplicati sulla chiave 'food_key'
before_count = len(df_food_dimension)
df_food_dimension = df_food_dimension.drop_duplicates(subset='food_key')
after_count = len(df_food_dimension)

# Verifica duplicati rimossi
print(f"Righe duplicate rimosse: {before_count - after_count}")
print("Nessun duplicato in food_key.")

# Salva il CSV finale
df_food_dimension.to_csv('datasets/food_dimension.csv', index=False)

print("food_dimension.csv creato con successo.")
print(f"Numero di righe nel file: {len(df_food_dimension)}")
