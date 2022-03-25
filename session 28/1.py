import numpy as np
a = np.array([3,2,-1])
f = np.poly1d(a)
print('f(-2)=',f(-2))
f1 = np.polyder(f,1)
print('f1(-2)=',f1(-2))
print('roots are:',f.r)