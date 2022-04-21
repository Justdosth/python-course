import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

data = np.array([[48,43],[29,44],[46,45],[73,45],[69,55],[51,57],[38,58],[54,58],
                [64,65],[60,68],[99,81],[99,82]])

linked = linkage(data,'single')
labellist = range(1,13)
dendrogram(linked,labels=labellist)
plt.show()

model = AgglomerativeClustering(n_clusters=2)
model.fit_predict(data)
plt.scatter(data[:,0], data[:,1],c=model.labels_)
plt.show()

