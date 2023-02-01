import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

x = np.arange(-5, 5, 0.01)

def diff_func(default, x):
    y, z = default

    dy_dx = y ** 2 * z
    dz_dx = z / x - y * z ** 2
    return dy_dx, dz_dx

y0 = 0
z0 = -3

default = y0, z0

sol = odeint(diff_func, default, x)

plt.plot(sol[:, 0], x, 'r', label='y(x)')
plt.plot(sol[:, 1], x, 'g', label='z(x)')

plt.legend()
plt.savefig('pic.png')
