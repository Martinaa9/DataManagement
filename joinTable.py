import pandas as pd
import os

def joinColumns(df1, df2, column1, column2):
    #This is the join
    df_joined = pd.merge(df1, df2, left_on=column1, right_on=column2)
    #Now I drop the column that is duplicated
    df_joined = df_joined.drop(column2, axis=1)
    return df_joined



df_indian_food = pd.read_csv('datasets/indian_food.csv')
df_fast_food = pd.read_csv('datasets/Datafiniti_Fast_Food_Restaurants.csv') #
df_nutrition = pd.read_csv('datasets/nutrients_csvfile.csv')
df_fastFoodNutrition = pd.read_csv('datasets/FastFoodNutritionMenuV2.csv') #
df_food_dataset = pd.read_csv('datasets/food_coded.csv')

#print(df_indian_food['name'])

#print(df_fast_food['name'])
#print(df_fastFoodNutrition['Company'])

joinedTable = joinColumns(df_fastFoodNutrition, df_fast_food, 'Company', 'name')
print(joinedTable)

#I want to write a file with the columns of the joined table
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



