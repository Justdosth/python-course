import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

data = {'gender':[1,1,1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1],
        'age':[39,40,41,42,43,43,44,44,46,47,47,47,48,49,50,50,50,49,48,47,46,45,44,44],
        'smoke':[0,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0],
        'cancer':[0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0]
        }

df = pd.DataFrame(data,columns=data.keys())
x = df[['gender','age','smoke']]
y = df['cancer']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=123)
error = []
for i in range(1,21):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(x_train,y_train)
    ypred=model.predict(x_test)
    error.append(np.mean(ypred!=y_test))

least_error = min(error)
model = KNeighborsClassifier(n_neighbors=error.index(least_error)+1)
model.fit(x,y)
ypred = model.predict([[0,45,1]])
if ypred:
    print('she has cancer')
else:
    print('she doesn\'t have cancer')