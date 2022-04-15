import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split


data = np.array([[10,1,0],[20,2,0],[30,2,0],[30,3,1],[35,1,0],[35,2,1],[40,1,0],[45,1,1],[45,2,0],
                [45,3,0],[50,1,0],[50,2,0],[40,1,1],[50,3,1],[55,1,1],[55,1,0],[60,1,0],
                [60,2,1],[70,1,1],[70,1,0],[70,2,1],[75,1,1],[80,2,1],[85,1,1],[85,2,1],
                [90,1,1],[90,2,1],[95,1,1],[100,1,1],[65,2,1],[50,1,0],[50,2,1],[45,1,0]])

x = data[:,:-1]
y = data[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=123)
model = LogisticRegression()
model.fit(x_train,y_train)

ypred = model.predict(x_test)
print('accurancy is',metrics.accuracy_score(y_test, ypred)*100,'%')

y_pred = model.predict([[40,2]])

if y_pred:
    print('this student will pass')
else:
    print('this student will fail')