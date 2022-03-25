import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,12.5,13,15,17,17.5,19])
y = np.array([7,17,15,12,18,19,20])

plt.plot(x,y)
plt.xlabel('study hours')
plt.ylabel('grade')
plt.show()
