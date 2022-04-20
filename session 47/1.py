import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = np.array([[13.2,236,58,21.2],[10,263,48,44.5],
                 [8.1,294,80,31],[8.8,190,50,19.5],
                 [9,276,91,40.6],[7.9,204,78,38.7],
                 [3.3,110,77,11.1],[5.9,238,72,15.8],
                 [15.4,335,80,31.9],[17.4,211,60,25.8],
                 [5.3,46,83,20.2],[2.6,120,54,14.2],
                 [10.4,249,83,24],[7.2,113,65,21],
                 [2.2,56,57,11.3]])
nations = ['Alabama','Alaska','Arizona','Arkankas','California',
           'Colorado','Connecticut','Delaware','Florida','Geirgia',
           'Hawaii','Idaho','Illinois','Indiana','Iowa']
se = []
for i in range(1,15):
    model = KMeans(n_clusters=i)
    model.fit(data)
    se.append(model.inertia_)

plt.plot(range(1,15),se)
plt.show()

print('the best number of cluster is 3 for this problem')
best_k = 3 #according to the plot

model = KMeans(n_clusters=best_k)
model.fit(data)
labels = model.labels_
cluster_0 = []
cluster_1 = []
cluster_2 = []
for i in range(15):
    # print(f'{nations[i]} is in the {labels[i]+1} cluster')
    if (labels[i]==0):
        cluster_0.append(nations[i])
    elif (labels[i]==1):
        cluster_1.append(nations[i])
    else:
        cluster_2.append(nations[i])

print(f'cluster 1 have {cluster_0} nations')
print(f'cluster 2 have {cluster_1} nations')
print(f'cluster 3 have {cluster_2} nations')