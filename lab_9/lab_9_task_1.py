import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 180, 0.1)

def bacteria_function(amount, t):
    dNdt = k * amount
    return dNdt

N_0 = 1
k = 1 / 20

N_t = odeint(bacteria_function, N_0, t)

plt.plot(t, N_t[:,0], label='Caulobacter Crescentus')
plt.xlabel('Время размножение, секунды')
plt.ylabel('Количество бактерий, штуки')
plt.title('Размножение бактерий')
plt.legend()

plt.savefig('pic.png')
