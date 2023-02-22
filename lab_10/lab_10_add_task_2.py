import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

x = np.arange(0.01, 5, 0.01)

def diff_func(default, x):
    y, w = default

    dy_dx = w
    dw_dx = w ** 2 / y - 3 * y / x ** 0.5 # Неправильно выведено
    return dy_dx, dw_dx

y0 = 0.01
w0 = 1

default = y0, w0

sol = odeint(diff_func, default, x)

plt.plot(sol[:, 0], x, 'b', label='y(x)')
plt.plot(sol[:, 1], x, 'y', label='w(x)')

plt.legend()
plt.savefig('pic.png')

# Возникает ошибка
