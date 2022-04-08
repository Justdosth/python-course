from scipy.integrate import quad
import numpy as np

def f(x):
    return x*np.exp(2*x)

a = 0
b = 1
int_f = quad(f,a,b)
print(int_f[0],'is integral for x*np.exp(2*x)')
