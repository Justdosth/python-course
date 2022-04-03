import pandas as pd
data = {'physics':[18,12,19],'chemistery':[16.25,15,20],
'mathematics':[14,13,18],'literature':[17,15,17]}
y = pd.DataFrame(data,index=['Ali','Mohammad','Reza'])
writer = pd.ExcelWriter('session 33/grades.xlsx',engine='xlsxwriter')
y.to_excel(writer,sheet_name='lesson_grade')
writer.save()
print(y)