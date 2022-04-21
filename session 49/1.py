import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import OPTICS

dataset = pd.read_excel('session 49/Mall_Customers.xlsx')

data = dataset.iloc[:,[3,4]].values
# plt.scatter(data[:,0],data[:,1],s=10,c='black')

model = OPTICS(min_samples=4)
labels = model.fit_predict(data)

plt.scatter(data[labels == -1,0], data[labels == -1, 1], s = 10, c = 'black')
plt.scatter(data[labels == 0,0], data[labels == 0, 1], s = 10, c = 'blue')
plt.scatter(data[labels == 1,0], data[labels == 1, 1], s = 10, c = 'red')
plt.scatter(data[labels == 2,0], data[labels == 2, 1], s = 10, c = 'green')
plt.scatter(data[labels == 3,0], data[labels == 3, 1], s = 10, c = 'brown')
plt.scatter(data[labels == 4,0], data[labels == 4, 1], s = 10, c = 'pink')
plt.scatter(data[labels == 5,0], data[labels == 5, 1], s = 10, c = 'yellow')
plt.scatter(data[labels == 6,0], data[labels == 6, 1], s = 10, c = 'silver')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()