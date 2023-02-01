import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(-5, 5, 0.01)

def diff_func(default, t):
    y, w = default

    dw_dt = np.sin(t) + np.cos(t)
    dy_dt = w
    return dw_dt, dy_dt

w0 = 0
y0 = 3

default = w0, y0

sol = odeint(diff_func, default, t)

plt.plot(sol[:, 0], t, 'r', label='w(t)')
plt.plot(sol[:, 1], t, 'b', label='y(t)')

plt.legend()
plt.savefig('pic.png')
