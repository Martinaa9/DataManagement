import os
import pandas as pd
import kagglehub
from kaggle.api.kaggle_api_extended import KaggleApi


# Funzione per scaricare i dataset tramite API
def download_datasets():
    api = KaggleApi()
    api.authenticate()

    # Lista dei dataset da scaricare
    datasets = [
        "nehaprabhavalkar/indian-food-101",
        "imtkaggleteam/fast-food-restaurants-across-america",
        "markmedhat/food-dataset"
    ]

    # Creare una cartella per i dataset se non esiste
    os.makedirs("datasets", exist_ok=True)

    # Scaricare tutti i dataset nella cartella 'datasets'
    for dataset in datasets:
        print(f"Scaricando {dataset}...")
        api.dataset_download_files(dataset, path="datasets/", unzip=True)

    print("Download completato per i dataset via API! ✅ I file si trovano nella cartella 'datasets'.")

# Funzione per caricare i dataset scaricati
def load_datasets():
    try:
        # Tentiamo di caricare i file CSV/TSV con gestione delle righe problematiche
        df_indian_food = pd.read_csv('datasets/indian_food.csv')  
        df_fast_food = pd.read_csv('datasets/Datafiniti_Fast_Food_Restaurants.csv')  
     #   df_food_dataset = pd.read_csv('datasets/food_dataset.csv')  
        # Caricare il quarto dataset scaricato manualmente (CSV)
        #df_food_waste = pd.read_csv('C:/Users/hp/DataManagement/Food Waste data and research - by country.csv')

        # Mostrare le prime righe dei dataframe per verificare che siano caricati correttamente

       # print("\nIndian Food Dataset:")
       # print(df_indian_food.head())

       # print("\nFast Food Restaurants Dataset:")
       # print(df_fast_food.head())
        

        print("\nIndian Food Dataset:")
        #I need to take one columnc from df_indian_food
        df_indian_food = df_indian_food[['name','ingredients','diet','prep_time','cook_time','flavor_profile','course','state','region']]
        #I want to print only the columns region
        print(df_indian_food['state'])
        
        return df_indian_food, df_fast_food
    
    except Exception as e:
        print(f"Errore nel caricamento dei dataset: {e}")

# Scaricare i dataset
download_datasets()

# Caricare i dataset
df_indian_food, df_fast_food = load_datasets()

df_food_dataset = pd.read_csv('datasets/food_coded.csv')  
#I need to take one columnc from df_food_dataset
df_food_dataset = df_food_dataset
print("*************************")
print("\nFood Dataset:")
print(df_food_dataset['GPA'])