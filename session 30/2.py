import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1,0.00001)
y = np.sqrt(1 - x**2)

plt.plot(x, y,'y')
plt.plot(x, -y,'y')
plt.gca().set_aspect('equal')
plt.show()
