from scipy.optimize import curve_fit as cf
import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b):
    return 1 / (a + b*x)

x = np.linspace(-2,2,40)
y = f(x,a=2,b=2)+0.2*np.random.normal(size=(40))

popt,pcov = cf(f,x,y)
a,b = popt
ypred = f(x,a,b)

plt.plot(x,y,'o',label='data')
plt.plot(x,ypred,label='fit')
plt.legend()
plt.show()
