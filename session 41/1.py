import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

x = [[60,80,40,75,90,35,50,80,100,50],[2,2,1,2,3,1,1,2,3,1],[4,2,1,2,4,1,3,5,4,1]
,[10,5,15,5,10,2,10,5,10,2],[1,1,1,2,2,2,2,3,3,3]]
x = np.array(x)
x = x.T
y = [620,920,360,1125,1170,560,700,1600,1800,1000]

model = LinearRegression()
model.fit(x,y)
ypred = model.predict([[70,1,2,17,2]])
print(ypred)