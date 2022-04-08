from scipy.integrate import quad
import numpy as np

def f(x):
    return np.cos(x)**2 * np.sin(x)

a = 0
b = np.pi/2
int_f = quad(f,a,b)
print(int_f[0],'is integral for np.cos(x)**2 * np.sin(x)')
