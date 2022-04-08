from scipy.integrate import quad
import numpy as np

def f(x):
    return np.log(x)/x

a = 2
b = 3
int_f = quad(f,a,b)
print(int_f[0],'is integral for np.log(x)/x')
