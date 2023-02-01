import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(-1, 1, 0.01)

def diff_func(default, t):
    x, y, z = default

    dx_dt = 3 * x - y + z
    dy_dt = x + y + z
    dz_dt = 4 * x - y + 4 * z
    return dx_dt, dy_dt, dz_dt

x0 = -71
y0 = 1
z0 = -3

default = x0, y0, z0

sol = odeint(diff_func, default, t)

plt.plot(sol[:, 0], t, 'r', label='x(t)')
plt.plot(sol[:, 1], t, 'g', label='y(t)')
plt.plot(sol[:, 2], t, 'b', label='z(t)')

plt.legend()
plt.savefig('pic.png')
