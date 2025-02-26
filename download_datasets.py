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
        "niharika41298/nutrition-details-for-most-common-foods",
        #"utkarshsaxenadn/fast-food-nutrition-eda-data-analysis",
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
        df_waste_food = pd.read_csv('datasets/Food Waste data and research - by country.csv')
        df_FastFoodNutrition = pd.read_csv('datasets/FastFoodNutritionMenuV2.csv')

        # Selezione di alcune colonne per il dataset indiano
        #df_indian_food = df_indian_food[['name','ingredients','diet','prep_time','cook_time','flavor_profile','course','state','region']]
        #print("Stato (Indian Food):")
        #print(df_indian_food['state'])
        
        return df_indian_food, df_fast_food, df_nutrition, df_waste_food, df_FastFoodNutrition
    
    except Exception as e:
        print(f"Errore nel caricamento dei dataset: {e}")

# Funzione per pulire i dataset eliminando duplicati e valori nulli
def clean_datasets(datasets):
    cleaned_datasets = []  # Lista per memorizzare i dataset puliti

    for df in datasets:
        df_cleaned = df.drop_duplicates().dropna()  # Rimuove duplicati e valori nulli
        cleaned_datasets.append(df_cleaned)  # Aggiungi il DataFrame pulito alla lista
    
    return cleaned_datasets

# Scaricare i dataset
download_datasets()

# Caricare i dataset
df_indian_food, df_fast_food, df_nutrition, df_waste_food, df_FastFoodNutrition = load_datasets()


#Eliminazione colonne non utili 
df_indian_food.drop(columns=['cook_time', 'prep_time'], inplace=True)
df_indian_food.to_csv("datasets/indian_food.csv", index=False)  # Sovrascrive il file originale

df_nutrition.drop(columns=['Sat.Fat', 'Fiber'], inplace=True)
df_nutrition.to_csv("datasets/nutrients_csvfile.csv", index=False)

df_fast_food.drop(columns=['keys', 'websites', 'dateAdded','dateUpdated', 'address', 'sourceURLs'], inplace=True)
df_fast_food.to_csv("datasets/FastFoodRestaurants.csv", index=False)

#df_waste_food.drop(columns=['M49 code','Source'],inplace=True)
#df_waste_food.to_csv('datasets/Food Waste data and research - by country.csv', index=False)

#df_FastFoodNutrition.drop(columns=['Calories from\nFat', 'Saturated Fat\n(g)', 'Trans Fat\n(g)', 'Cholesterol\n(mg)','Sodium \n(mg)','Fiber\n(g)','Sugars\n(g)','Weight Watchers\nPnts'], inplace=True)
#df_FastFoodNutrition.to_csv("datasets/FastFoodNutritionMenuV2.csv", index=False)
#Pulire i nomi delle colonne eliminando "\n" e spazi extra e "(g)" dai nomi delle colonne + modifica nome fat 
df_FastFoodNutrition.columns = df_FastFoodNutrition.columns.str.replace("\n", " ") \
    .str.replace("(g)", "", regex=False) \
    .str.replace("Total Fat", "Fat") \
    .str.strip()
df_FastFoodNutrition.to_csv("datasets/FastFoodNutritionMenuV2.csv", index=False)


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
        f.write("\nFast food nutrition columns:\n")
        for col in df_FastFoodNutrition.columns:
            f.write(f"- {col}\n")
        f.write("\nFood waste columns:\n")
        for col in df_waste_food.columns:
            f.write(f"- {col}\n")
    print(f"Elenco delle colonne salvato in '{filename}'.")

# Creare il file con l'elenco delle colonne
write_columns_to_file("column_names.txt")
