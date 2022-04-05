import pandas as pd
data = {'physics':[18,12,19],'chemistery':[16.25,15,20],
'mathematics':[14,13,18],'literature':[17,15,17]}
y = pd.DataFrame(data,index=['Ali','Mohammad','Reza'])
print(y.describe())
print("=================================================")
print(y.corr())