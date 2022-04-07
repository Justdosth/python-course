from scipy.optimize import curve_fit as cf
import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b,c):
    return a * x**b + c

x = np.linspace(1,8,60)
y = f(x,a=1,b=2,c=2) + 0.2*np.random.normal(size=(60))

popt,pcov = cf(f,x,y)
a,b,c = popt
ypred = f(x,a,b,c)

plt.plot(x,y,'o',label='data')
plt.plot(x,ypred,label='fit')
plt.legend()
plt.show()
