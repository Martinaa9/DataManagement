import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Funzione per scaricare i dataset tramite API
def download_datasets():
    api = KaggleApi()
    api.authenticate()

    # Lista dei dataset da scaricare
    datasets = [
        "nehaprabhavalkar/indian-food-101",
        "imtkaggleteam/fast-food-restaurants-across-america",
        "markmedhat/food-dataset",
        "niharika41298/nutrition-details-for-most-common-foods",
        # "utkarshsaxenadn/fast-food-nutrition-eda-data-analysis",
    ]

    # Creare una cartella per i dataset se non esiste
    os.makedirs("datasets", exist_ok=True)

    # Scaricare tutti i dataset nella cartella 'datasets'
    for dataset in datasets:
        try:
            print(f"Scaricando {dataset}...")
            api.dataset_download_files(dataset, path="datasets/", unzip=True)
            print(f"Dataset {dataset} scaricato con successo!")
        except Exception as e:
            print(f"Errore durante il download del dataset {dataset}: {e}")

# Funzione per caricare i dataset scaricati
def load_datasets():
    try:
        # Caricamento dei dataset
        df_indian_food = pd.read_csv('datasets/indian_food.csv')
        df_fast_food = pd.read_csv('datasets/Datafiniti_Fast_Food_Restaurants.csv')
        df_nutrition = pd.read_csv('datasets/nutrients_csvfile.csv')

        # Selezione di alcune colonne per il dataset indiano
        df_indian_food = df_indian_food[['name','ingredients','diet','prep_time','cook_time','flavor_profile','course','state','region']]
        print("Stato (Indian Food):")
        print(df_indian_food['state'])
        
        return df_indian_food, df_fast_food, df_nutrition
    
    except Exception as e:
        print(f"Errore nel caricamento dei dataset: {e}")

# Scaricare i dataset
download_datasets()

# Caricare i dataset
df_indian_food, df_fast_food, df_nutrition = load_datasets()

# Caricare un ulteriore dataset
df_food_dataset = pd.read_csv('datasets/food_coded.csv')
print("*************************")
print("\nFood Dataset:")
print(df_food_dataset['GPA'])

# Funzione per scrivere in un file i nomi delle colonne di ogni dataset
def write_columns_to_file(filename):
    with open(filename, "w") as f:
        f.write("Indian Food Dataset columns:\n")
        for col in df_indian_food.columns:
            f.write(f"- {col}\n")
        f.write("\nFast Food Restaurants Dataset columns:\n")
        for col in df_fast_food.columns:
            f.write(f"- {col}\n")
        f.write("\nNutrition Dataset columns:\n")
        for col in df_nutrition.columns:
            f.write(f"- {col}\n")
        f.write("\nFood Dataset columns:\n")
        for col in df_food_dataset.columns:
            f.write(f"- {col}\n")
    print(f"Elenco delle colonne salvato in '{filename}'.")

# Creare il file con l'elenco delle colonne
write_columns_to_file("column_names.txt")
