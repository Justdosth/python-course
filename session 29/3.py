import matplotlib.pyplot as plt
import numpy as np

x2 = np.array([40,55,60,73,89,100,110])
y2 = np.array([500,710,750,890,1100,1500,1600])
y3 = np.array([700,900,990,1200,1550,1800,1900])
y4 = np.array([1000,1230,1400,1900,2500,3000,3700])

plt.plot(x2,y2,label='1')
plt.plot(x2,y3,label='2')
plt.plot(x2,y4,label='3')
plt.xlabel('meters')
plt.ylabel('price')
plt.legend()
plt.show()