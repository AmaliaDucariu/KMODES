from string import digits
import pandas as pd
import numpy as np

def no_space_to_lower(arr):
    new_arr = []
    remove_digits = str.maketrans('', '', digits)
    for element in arr:
        element = element.lower()
        element = element.replace(" ", "")
        element = element.replace(",", "")
        element = element.replace(".", "")
        element = element.replace("/", "")
        element = element.replace("(", "")
        element = element.replace(")", "")
        element = element.replace("'", "")
        element = element.replace("|", "")
        element = element.replace("-", "")
        element = element.translate(remove_digits)
        new_arr.append(element)
    return new_arr


def getNumberArr(int):
    new_arr = []
    for i in range(int):
        new_arr.append(i)
    return new_arr


dataset1 = pd.read_csv('C:\\Dizertation FINAL\\Data Sets\\naukri_data_science_jobs_india.csv')

dataset1.Job_Role.fillna('', inplace=True)
dataset1.Company.fillna('', inplace=True)
dataset1.Location.fillna('', inplace=True)
Job_Role = np.array(dataset1['Job_Role'])
Company = np.array(dataset1['Company'])
Location = np.array(dataset1['Location'])
Job_Role = no_space_to_lower(Job_Role)
Company = no_space_to_lower(Company)
Location = no_space_to_lower(Location)
Number = getNumberArr(12000)

final_dataset1 = pd.DataFrame({'Number': Number, 'Job_Role': Job_Role, 'Company': Company, 'Location': Location})

final_dataset1.to_excel('C:\\Dizertation FINAL\\Data Sets\\Jobs_Prelucrat.xlsx')

dataset2 = pd.read_csv('C:\\Dizertation FINAL\\Data Sets\\food_ingredients_and_allergens.csv')

dataset2.Food_Product.fillna('', inplace=True)
dataset2.Main_Ingredient.fillna('', inplace=True)
dataset2.Sweetener.fillna('', inplace=True)
dataset2.Fat_Oil.fillna('', inplace=True)
dataset2.Seasoning.fillna('', inplace=True)
dataset2.Allergens.fillna('', inplace=True)
Food_Product = np.array(dataset2['Food_Product'])
Main_Ingredient = np.array(dataset2['Main_Ingredient'])
Sweetener = np.array(dataset2['Sweetener'])
Fat_Oil = np.array(dataset2['Fat_Oil'])
Seasoning = np.array(dataset2['Seasoning'])
Allergens = np.array(dataset2['Allergens'])
Food_Product = no_space_to_lower(Food_Product)
Main_Ingredient = no_space_to_lower(Main_Ingredient)
Sweetener = no_space_to_lower(Sweetener)
Fat_Oil = no_space_to_lower(Fat_Oil)
Seasoning = no_space_to_lower(Seasoning)
Allergens = no_space_to_lower(Allergens)

final_dataset2 = pd.DataFrame({'Food_Product': Food_Product, 'Main_Ingredient': Main_Ingredient, 'Sweetener': Sweetener, 'Fat_Oil': Fat_Oil, 'Seasoning': Seasoning, 'Allergens': Allergens})

final_dataset2.to_excel('C:\\Dizertation FINAL\\Data Sets\\Food_Prelucrat.xlsx')