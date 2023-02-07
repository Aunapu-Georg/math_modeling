import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = 123456789
R = 6371000
M = 5.9742 * 10 ** 24
r_0 = R + h
v_0 = 0.1
G = 6.674 * 10**(-11)

r = np.linspace(r_0, 0, 100)

def meteorite_function(v, r):
    dvdr = G * M / (v * (h + R - r) ** 2)
    return dvdr

v_r = odeint(meteorite_function, v_0, r)


plt.plot(r, v_r[:, 0], label='Гоба')
plt.xlabel('Расстояние до поверхности Земли, м')
plt.ylabel('Скорость метеорита, метров в секунду')
plt.title('Падение метеорита')
plt.legend()

plt.savefig('pic.png')
