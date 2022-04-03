import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([20,100,250,400,420,440,510])
y1 = np.array([120,300,700,1000,1100,1500,2000])

plt.plot(x1,y1,'-o')
plt.xlabel('tempreture')
plt.ylabel('pressure')
plt.show()

