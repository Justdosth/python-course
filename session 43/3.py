import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


data = np.array([[10,1,0],[20,2,0],[30,2,0],[30,3,1],[35,1,0],[35,2,1],[40,1,0],[45,1,1],[45,2,0],
                [45,3,0],[50,1,0],[50,2,0],[40,1,1],[50,3,1],[55,1,1],[55,1,0],[60,1,0],
                [60,2,1],[70,1,1],[70,1,0],[70,2,1],[75,1,1],[80,2,1],[85,1,1],[85,2,1],
                [90,1,1],[90,2,1],[95,1,1],[100,1,1],[65,2,1],[50,1,0],[50,2,1],[45,1,0]])

x = data[:,:-1]
y = data[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=123)
error = []
for i in range(1,29):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(x_train,y_train)
    ypred=model.predict(x_test)
    error.append(np.mean(ypred!=y_test))

least_error = min(error)
model = KNeighborsClassifier(n_neighbors=error.index(least_error)+1)
model.fit(x,y)
ypred = model.predict([[40,2]])
if ypred:
    print('the student will pass')
else:
    print('the student will fail')