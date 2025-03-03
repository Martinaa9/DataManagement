import pandas as pd
import numpy as np  # Importiamo numpy per usare ceil

# Caricamento dei dataset 
df_indian_food = pd.read_csv('datasets/indian_food.csv')
df_nutrition = pd.read_csv('datasets/nutrients_csvfile.csv')

# Normalizziamo i nomi degli ingredienti e dei cibi nutrizionali per evitare problemi di maiuscole e spazi
df_nutrition["Food"] = df_nutrition["Food"].str.lower().str.strip()
df_indian_food["ingredients"] = df_indian_food["ingredients"].str.lower().str.strip()

# Convertiamo le colonne in formato numerico, con 'NaN' per valori non validi
df_nutrition["Calories"] = pd.to_numeric(df_nutrition["Calories"], errors='coerce')
df_nutrition["Protein"] = pd.to_numeric(df_nutrition["Protein"], errors='coerce')
df_nutrition["Fat"] = pd.to_numeric(df_nutrition["Fat"], errors='coerce')
df_nutrition["Carbs"] = pd.to_numeric(df_nutrition["Carbs"], errors='coerce')
df_nutrition["Grams"] = pd.to_numeric(df_nutrition["Grams"], errors='coerce')

# Funzione per calcolare la somma dei valori nutrizionali per 1 grammo
def calcola_valori_nutrizionali(ingredienti):
    # Convertiamo la stringa degli ingredienti in una lista
    ingredienti_lista = [ing.strip() for ing in ingredienti.split(",")]
    
    # Filtra il dataset nutrizionale per gli ingredienti trovati
    df_match = df_nutrition[df_nutrition["Food"].isin(ingredienti_lista)]
    
    # Assicuriamoci che la colonna 'Grams' non contenga valori nulli o vuoti
    df_match = df_match.dropna(subset=["Grams"])  # Rimuoviamo righe con 'NaN' nei grammi
    
    # Normalizziamo i valori nutrizionali dividendo per la colonna 'Grams' per ottenere i valori su base 1 grammo
    if not df_match.empty:  # Verifica che non ci siano ingredienti non trovati nel database nutrizionale
        df_match["Calories"] = df_match["Calories"] / df_match["Grams"]
        df_match["Protein"] = df_match["Protein"] / df_match["Grams"]
        df_match["Fat"] = df_match["Fat"] / df_match["Grams"]
        df_match["Carbs"] = df_match["Carbs"] / df_match["Grams"]
    
        # Somma i valori nutrizionali per tutti gli ingredienti trovati
        total_calories = df_match["Calories"].sum()
        total_protein = df_match["Protein"].sum()
        total_fat = df_match["Fat"].sum()
        total_carbs = df_match["Carbs"].sum()

        # Arrotondiamo per eccesso
        total_calories = np.ceil(total_calories)  # Arrotonda per eccesso
        total_protein = np.ceil(total_protein)    # Arrotonda per eccesso
        total_fat = np.ceil(total_fat)            # Arrotonda per eccesso
        total_carbs = np.ceil(total_carbs)        # Arrotonda per eccesso

        # Convertiamo i valori in interi (senza decimali)
        total_calories = int(total_calories)
        total_protein = int(total_protein)
        total_fat = int(total_fat)
        total_carbs = int(total_carbs)

        return {
            "total_calories": total_calories,
            "total_protein": total_protein,
            "total_fat": total_fat,
            "total_carbs": total_carbs
        }
    else:
        # Se non ci sono ingredienti trovati nel database, restituiamo 0 per tutti i valori
        return {
            "total_calories": 0,
            "total_protein": 0,
            "total_fat": 0,
            "total_carbs": 0
        }

# Applichiamo la funzione a ogni riga del dataset
df_indian_food[["total_calories", "total_protein", "total_fat", "total_carbs"]] = df_indian_food["ingredients"].apply(lambda x: pd.Series(calcola_valori_nutrizionali(x)))

# Salviamo il nuovo dataset con i valori nutrizionali calcolati
df_indian_food.to_csv("cibo_con_valori_nutrizionali.csv", index=False)

print("Join completato! Il file è stato salvato come 'cibo_con_valori_nutrizionali.csv'")
