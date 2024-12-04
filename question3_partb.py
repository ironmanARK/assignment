import numpy as np
from scipy.integrate import quad
def f(t, r):
    x =r*np.cos(t)
    y= r*np.sin(t)
    return x**2 + y**4
r=np.sqrt(3)
integral, error =quad(f, 0, 2 * np.pi, args=(r,))
print(integral)
