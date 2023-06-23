import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt

culoare_par = np.array(['blond', 'brunet', 'roscat', 'negru', 'brunet', 'negru', 'roscat', 'negru'])
culoare_ochi = np.array(['caprui', 'gri', 'verde', 'albastru', 'caprui', 'gri', 'verde', 'albastru'])
culoare_tricou = np.array(['galben', 'negru', 'mov', 'galben', 'albastru', 'brown', 'mov', 'mov'])
persoana = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
data = pd.DataFrame({'persoana': persoana, 'culoare_par': culoare_par, 'culoare_ochi': culoare_ochi, 'culoare_tricou': culoare_tricou})
data = data.set_index('persoana')

cost = []
K = range(1, 5)
for num_clusters in list(K):
    kmode = KModes(n_clusters=num_clusters, init="random", n_init=5, verbose=1)
    kmode.fit_predict(data)
    cost.append(kmode.cost_)

plt.plot(K, cost, 'bx-')
plt.xlabel('No. of clusters')
plt.ylabel('Cost')
plt.title('Elbow Method For Optimal k')
plt.show()

kmode = KModes(n_clusters=3, init = "random", n_init = 5, verbose=1)
clusters = kmode.fit_predict(data)

data.insert(0, "Cluster", clusters, True)
print(data)
