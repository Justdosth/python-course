from scipy.optimize import curve_fit as cf
import numpy as np
import matplotlib.pyplot as plt

def f(x,A,w,phi):
    return A*np.sin(w*x + phi)

x = np.linspace(-5,5,60)
y = f(x,A=2,w=0.2*np.pi,phi=20)+0.2*np.random.normal(size=(60))

popt,pcov = cf(f,x,y)
a,b,c = popt
ypred = f(x,a,b,c)

plt.plot(x,y,'o',label='data')
plt.plot(x,ypred,label='fit')
plt.legend()
plt.show()
