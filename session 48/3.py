import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN

X = np.array([[13.2,236,58,21.2],[10,263,48,44.5],
                 [8.1,294,80,31],[8.8,190,50,19.5],
                 [9,276,91,40.6],[7.9,204,78,38.7],
                 [3.3,110,77,11.1],[5.9,238,72,15.8],
                 [15.4,335,80,31.9],[17.4,211,60,25.8],
                 [5.3,46,83,20.2],[2.6,120,54,14.2],
                 [10.4,249,83,24],[7.2,113,65,21],
                 [2.2,56,57,11.3]])

neighbors = NearestNeighbors(n_neighbors=2)
neighbors_fit = neighbors.fit(X)
distances , indices = neighbors_fit.kneighbors(X)
distance = np.sort(distances,axis=0)
distances = distance[:,1]
plt.plot(distances)
plt.show()

model = DBSCAN(eps=30,min_samples=2)
model.fit(X)
print(model.labels_)