import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

x = np.array([[120,50,1],
              [60,20,2],
              [145,65,1],
              [130,45,3],
              [50,15,2]])
se = []
for i in range(1,5):
    model = KMeans(n_clusters=i)
    model.fit(x)
    se.append(model.inertia_)

plt.plot(range(1,5),se)
plt.xlabel('clusters')
plt.ylabel('elbow')
plt.show()

sc = []
for i in range(2,5):
    model = KMeans(n_clusters=i)
    model.fit(x)
    s = silhouette_score(x, model.labels_)
    sc.append(s)

plt.plot(range(2,5),sc)
plt.xlabel('clusters')
plt.ylabel('silhouette')
plt.show()