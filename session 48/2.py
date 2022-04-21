import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN

X = np.array([[120, 50, 1],[60, 20, 2],[145, 65, 1],[130, 45, 3], [50, 15, 2]])

neighbors = NearestNeighbors(n_neighbors=2)
neighbors_fit = neighbors.fit(X)
distances , indices = neighbors_fit.kneighbors(X)
distance = np.sort(distances,axis=0)
distances = distance[:,1]
plt.plot(distances)
plt.show()

model = DBSCAN(eps=12,min_samples=2)
model.fit(X)
print(model.labels_)