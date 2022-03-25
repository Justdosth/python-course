import numpy as np
x = [[1,2],[-1,-2]]
x = np.array(x)
y = [[3,4],[-3,-4]]
y = np.array(y)
print('2D array stacked with axis=0:\n',np.stack((x,y),axis=0))
print('2D array stacked with axis=1:\n',np.stack((x,y),axis=1))
print('2D array h_stacked:\n',np.hstack((x,y)))
print('2D array v_stacked:\n',np.vstack((x,y)))
print('2D array d_stacked:\n',np.dstack((x,y)))