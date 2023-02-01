import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(-1, 1, 0.01)

def diff_func(default, t):
    x, y = default

    dx_dt = 3 * x - 2 * y + np.e ** (3 * t) / np.e ** t + 1
    dy_dt = x - np.e ** (3 * t) / np.e ** t + 1
    return dx_dt, dy_dt

x0 = 5
y0 = -7

default = x0, y0

sol = odeint(diff_func, default, t)

plt.plot(sol[:, 0], t, 'r', label='x(t)')
plt.plot(sol[:, 1], t, 'y', label='y(t)')

plt.legend()
plt.savefig('pic.png')
