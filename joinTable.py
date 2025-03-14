import pandas as pd
import numpy as np
import openpyxl
import os
from fuzzywuzzy import process

def clean_text(text):
    """Normalizza i testi eliminando spazi, convertendo in minuscolo e uniformando apostrofi."""
    return str(text).strip().lower().replace("’", "'").replace("`", "'")

def joinColumns(df1, df2, column1, column2):
    """Effettua il join tra due dataframe basato su colonne specifiche, con normalizzazione e fuzzy matching."""
    
    # Pulizia del testo nelle colonne da unire
    df1[column1] = df1[column1].apply(clean_text)
    df2[column2] = df2[column2].apply(clean_text)

    # Fuzzy matching per trovare corrispondenze migliori
    df1[column1] = df1[column1].apply(lambda x: process.extractOne(x, df2[column2].unique())[0] if isinstance(x, str) else x)

    # Merge dei dataframe
    df_joined = pd.merge(df1, df2, left_on=column1, right_on=column2, how="left")

    # Rimuovo la colonna duplicata
    df_joined = df_joined.drop(column2, axis=1)
    
    return df_joined

# Caricamento dei dataset
df_indian_food = pd.read_csv('datasets/indian_food.csv')
df_fast_food = pd.read_csv('datasets/Datafiniti_Fast_Food_Restaurants.csv')
df_nutrition = pd.read_csv('datasets/nutrients_csvfile.csv')
df_fastFoodNutrition = pd.read_csv('datasets/FastFoodNutritionMenuV2.csv')

df_fast_food = df_fast_food.drop(['dateAdded','dateUpdated','keys','sourceURLs','websites'], axis=1)

# Join tra Company e Name
joinedTable = joinColumns(df_fastFoodNutrition, df_fast_food, 'Company', 'name')

# Salva il file delle colonne
def write_columns_to_file(filename):
    with open(filename, "w") as f:
        f.write("Fast Food Nutrition Menu Dataset columns:\n")
        for col in df_fastFoodNutrition.columns:
            f.write(f"- {col}\n")
        f.write("\nFast Food Restaurants Dataset columns:\n")
        for col in df_fast_food.columns:
            f.write(f"- {col}\n")
        f.write("\nJoined Table columns:\n")
        for col in joinedTable.columns:
            f.write(f"- {col}\n")
    print(f"Elenco delle colonne salvato in '{filename}'.")

write_columns_to_file('columns.txt')

# Salvataggio dei dati uniti
joinedTable.to_csv('joinedTable.csv', index=False)

print("Tabella salvata in 'joinedTable.csv'")
