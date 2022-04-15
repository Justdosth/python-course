import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = {'gender':[1,1,1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1],
        'age':[39,40,41,42,43,43,44,44,46,47,47,47,48,49,50,50,50,49,48,47,46,45,44,44],
        'smoke':[0,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0],
        'cancer':[0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0]
        }
df = pd.DataFrame(data,columns=data.keys())
x = df[['gender','age','smoke']]
y = df['cancer']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=123)
model = LogisticRegression()
model.fit(x_train,y_train)

ypred = model.predict(x_test)
print(metrics.confusion_matrix(y_test, ypred))

print('Cancer chance for 45 year old smoking woman is',bool(model.predict([[0,45,1]])))

