import matplotlib.pyplot as plt
import numpy as np

x = ['physics','chemistry','mathematics','literature','english','idea!','sport']
y1 = [13,19,15,17,14,14,19]
y2 = [19,17,15,18,18.5,17,18]

plt.bar(x,y1,label='Reza')
plt.bar(x,y2,bottom=y1,label='Zahra')
plt.xlabel('lesson')
plt.ylabel('grade')
plt.legend()
plt.show()