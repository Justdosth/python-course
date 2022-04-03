import matplotlib.pyplot as plt
import numpy as np

x = ['physics','chemistry','mathematics','literature','english','idea!','sport']
y1 = [13,19,15,17,14,14,19]
y2 = [19,17,15,18,18.5,17,18]
x1 = np.arange(len(x))
w = 0.3
plt.bar(x1-w/2,y1,width=w,label='Reza')
plt.bar(x1+w/2,y2,width=w,label='Zahra')
plt.xlabel('lesson')
plt.ylabel('grade')
plt.xticks(x1,x)
plt.legend()
plt.show()