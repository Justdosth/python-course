import matplotlib.pyplot as plt
import numpy as np

x = np.arange(np.pi/2, np.pi*3/2,0.01)
y = 1 - np.cos(x)**2

plt.plot(x, y)
plt.show()