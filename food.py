import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
from datetime import datetime
import matplotlib.pyplot as plt


# Function to eliminate spaces and make everything lowercase
def no_space_to_lower(arr):
    new_arr = []
    for element in arr:
        element = element.replace(" ", "").lower()
        new_arr.append(element)
    return new_arr


# Defining the start time of the process
start_time = datetime.now()


# Importing dataset
dataset = pd.read_csv('C:\\Dizertation FINAL\\Data Sets\\food_ingredients_and_allergens.csv')

# Replace null values
dataset.Food_Product.fillna('', inplace=True)
dataset.Main_Ingredient.fillna('', inplace=True)
dataset.Sweetener.fillna('', inplace=True)
dataset.Fat_Oil.fillna('', inplace=True)
dataset.Seasoning.fillna('', inplace=True)
dataset.Allergens.fillna('', inplace=True)

# Data processing

Food_Product = np.array(dataset['Food_Product'])
Main_Ingredient = np.array(dataset['Main_Ingredient'])
Sweetener = np.array(dataset['Sweetener'])
Fat_Oil = np.array(dataset['Fat_Oil'])
Seasoning = np.array(dataset['Seasoning'])
Allergens = np.array(dataset['Allergens'])

Food_Product = no_space_to_lower(Food_Product)
Main_Ingredient = no_space_to_lower(Main_Ingredient)
Sweetener = no_space_to_lower(Sweetener)
Fat_Oil = no_space_to_lower(Fat_Oil)
Seasoning = no_space_to_lower(Seasoning)
Allergens = no_space_to_lower(Allergens)

# final_dataset_1 = pd.DataFrame({'Food_Product': Food_Product, 'Main_Ingredient': Main_Ingredient, 'Sweetener': Sweetener, 'Fat_Oil': Fat_Oil, 'Seasoning': Seasoning, 'Allergens': Allergens})
# final_dataset_1 = final_dataset_1.set_index('Food_Product')

# final_dataset_2 = pd.DataFrame({'Food_Product': Food_Product, 'Main_Ingredient': Main_Ingredient, 'Sweetener': Sweetener})
# final_dataset_2 = final_dataset_2.set_index('Food_Product')

final_dataset_3 = pd.DataFrame({'Food_Product': Food_Product, 'Main_Ingredient': Main_Ingredient, 'Sweetener': Sweetener, 'Fat_Oil': Fat_Oil})
final_dataset_3 = final_dataset_3.set_index('Food_Product')

cost = []
K = range(1, 5)
for num_clusters in list(K):
    kmode = KModes(n_clusters=num_clusters, init="random", n_init=5, verbose=1)
    kmode.fit_predict(final_dataset_3)
    cost.append(kmode.cost_)

# plt.plot(K, cost, 'bx-')
# plt.xlabel('No. of clusters')
# plt.ylabel('Cost')
# plt.title('Elbow Method For Optimal k')
# plt.show()

kmode = KModes(n_clusters=6, init = "random", n_init = 5, verbose=1)
clusters = kmode.fit_predict(final_dataset_3)

final_dataset_3.insert(0, "Cluster", clusters, True)
final_dataset_3.to_excel('C:\\Dizertation FINAL\\KModes results\\Food_Main_Ingredient_Sweetener_Fat_Oil_6.xlsx')

# Defining end time of the process and printing exec time
end_time = datetime.now()
time_difference = end_time - start_time
print("TIME INTERVAL:", time_difference)
