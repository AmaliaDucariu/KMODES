import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
from datetime import datetime
from string import digits
import matplotlib.pyplot as plt


# Function to eliminate spaces and make everything lowercase
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


# Defining the start time of the process
start_time = datetime.now()


# Importing dataset
dataset = pd.read_csv('C:\\Dizertation FINAL\\Data Sets\\naukri_data_science_jobs_india.csv')

# Replace null values
dataset.Job_Role.fillna('', inplace=True)
dataset.Company.fillna('', inplace=True)
dataset.Location.fillna('', inplace=True)

# Create column Number
Number = getNumberArr(12000)

# Data processing
Job_Role = np.array(dataset['Job_Role'])
Company = np.array(dataset['Company'])
Location = np.array(dataset['Location'])

Job_Role = no_space_to_lower(Job_Role)
Company = no_space_to_lower(Company)
Location = no_space_to_lower(Location)

# final_dataset_1 = pd.DataFrame({'Number': Number, 'Job_Role': Job_Role, 'Company': Company})
# final_dataset_1 = final_dataset_1.set_index('Number')

final_dataset = pd.DataFrame({'Number': Number, 'Job_Role': Job_Role, 'Company': Company, 'Location': Location})
final_dataset = final_dataset.set_index('Number')

cost = []
K = range(1, 5)
for num_clusters in list(K):
    kmode = KModes(n_clusters=num_clusters, init="random", n_init=5, verbose=1)
    kmode.fit_predict(final_dataset)
    cost.append(kmode.cost_)

# plt.plot(K, cost, 'bx-')
# plt.xlabel('No. of clusters')
# plt.ylabel('Cost')
# plt.title('Elbow Method For Optimal k')
# plt.show()

kmode = KModes(n_clusters=4, init = "random", n_init = 5, verbose=1)
clusters = kmode.fit_predict(final_dataset)

final_dataset.insert(0, "Cluster", clusters, True)
final_dataset.to_excel('C:\\Dizertation FINAL\\RESULTS NEW\JOBS KMODES\\Job_Role_Company_Location_4.xlsx')

# Defining end time of the process and printing exec time
end_time = datetime.now()
time_difference = end_time - start_time
print("TIME INTERVAL:", time_difference)
