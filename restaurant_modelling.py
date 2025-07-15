import pandas as pd

# Carica il file CSV originale
df_restaurants = pd.read_csv('datasets/FastFoodRestaurants.csv')

# Rimuove le colonne che non interessano
df_restaurants = df_restaurants.drop(columns=['id', 'categories'])

# Converte tutti i valori della tabella in minuscolo
df_restaurants = df_restaurants.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Crea la primary key composta chiamata 'restaurant_key'
df_restaurants['restaurant_key'] = (
    df_restaurants['city'].astype(str) + '_' +
    df_restaurants['latitude'].astype(str) + '_' +
    df_restaurants['longitude'].astype(str)
)

# Elimina i duplicati sulla chiave 'restaurant_key'
df_restaurants = df_restaurants.drop_duplicates(subset='restaurant_key')

# Porta 'restaurant_key' come prima colonna
cols = ['restaurant_key'] + [col for col in df_restaurants.columns if col != 'restaurant_key']
df_restaurants = df_restaurants[cols]

# Verifica che non ci siano più duplicati
duplicate_count = df_restaurants['restaurant_key'].duplicated().sum()
if duplicate_count > 0:
    print(f"Attenzione: ancora {duplicate_count} duplicati nella restaurant_key!")
else:
    print("Nessun duplicato nella restaurant_key — tutto OK.")

# Salva il nuovo CSV
df_restaurants.to_csv('datasets/restaurant_dimension.csv', index=False)

print("restaurant_dimension.csv creato con successo.")
print(f"Numero di righe nel file: {len(df_restaurants)}")