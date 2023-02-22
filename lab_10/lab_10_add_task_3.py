import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0.01, 5, 0.01)

def diff_func(default, t):
    y, w = default

    dy_dt = w
    dw_dt = np.sqrt(1 - w ** 2)
    return dy_dt, dw_dt

y0 = 3
w0 = 0

default = y0, w0

sol = odeint(diff_func, default, t)

plt.plot(sol[:, 0], t, 'r', label='y(t)')
plt.plot(sol[:, 1], t, 'b', label='w(t)')

plt.legend()
plt.savefig('pic.png')

# Возникает ошибка
