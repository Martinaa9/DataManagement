import pandas as pd

# Carica il file CSV originale
df_customer_fastfood = pd.read_csv('datasets/merged_customer_fastfood.csv')

# Rimuove le colonne non richieste
columns_to_drop = ['Educational_Qualifications', 'Family_size', 'Pin_code', 'Output', 'Feedback', 'Unnamed:_12']
df_customer_fastfood = df_customer_fastfood.drop(columns=columns_to_drop)

# Converte tutte le prime lettere dei nomi delle colonne in minuscolo
df_customer_fastfood.columns = [col.lower() for col in df_customer_fastfood.columns]

# Rinomina le colonne richieste (attenzione: ora sono tutte minuscole)
df_customer_fastfood = df_customer_fastfood.rename(columns={
    'calories': 'total_calories',
    'fat': 'total_fat',
    'carbs': 'total_carbs',
    'protein': 'total_protein'
})

# Converte tutte le stringhe delle celle in minuscolo (solo se di tipo stringa)
df_customer_fastfood = df_customer_fastfood.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Crea la customer_key concatenando customer_id, item e favorite_fastfood
df_customer_fastfood['customer_key'] = (
    df_customer_fastfood['customer_id'].astype(str) + '_' +
    df_customer_fastfood['item'].astype(str) + '_' +
    df_customer_fastfood['favorite_fastfood'].astype(str)
)

# Rimuove i duplicati sulla chiave 'customer_key'
df_customer_fastfood = df_customer_fastfood.drop_duplicates(subset='customer_key')

# Porta 'customer_key' come prima colonna
cols = ['customer_key'] + [col for col in df_customer_fastfood.columns if col != 'customer_key']
df_customer_fastfood = df_customer_fastfood[cols]

# Verifica che non ci siano più duplicati
duplicate_count = df_customer_fastfood['customer_key'].duplicated().sum()
if duplicate_count > 0:
    print(f"Attenzione: ancora {duplicate_count} duplicati nella customer_key!")
else:
    print("Nessun duplicato nella customer_key — tutto OK.")

# Salva il nuovo CSV
df_customer_fastfood.to_csv('datasets/customer_dimension.csv', index=False)

print("customer_dimension.csv creato con successo.")
print(f"Numero di righe nel file: {len(df_customer_fastfood)}")