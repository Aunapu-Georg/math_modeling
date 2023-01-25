import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 240, 0.1)

def material_function(velocity, t):
    dvdt = - gamma * velocity ** 2 / m + 9.8
    return dvdt

v_0 = 0
m = 70
gamma = 0.9

v_t = odeint(material_function, v_0, t)

plt.plot(t, v_t[:,0], label='Материальная точка')
plt.xlabel('Время с начала движения, секунд')
plt.ylabel('Скорость объекта, метров в секунду')
plt.title('Движение объекта с учётом сопротивления')
plt.legend()

plt.savefig('pic.png')
