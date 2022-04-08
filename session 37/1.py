from scipy.optimize import minimize
import numpy as np

def f(x):
    return x + np.exp(-x)

min_with_scipy = minimize(f, 0, method='BFGS')
print(min_with_scipy)

