import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 12, 0.1)

def invest_function(money, t):
    dMdt = - k * money * t
    return dMdt

M_0 = 1000
k = 0.08

M_t = odeint(invest_function, M_0, t)

plt.plot(t, M_t[:,0], label='Вклад')
plt.xlabel('Время с открытия производства, лет')
plt.ylabel('Сумма инвестиций, денежных единиц')
plt.title('Инвестиции в производство')
plt.legend()

plt.savefig('pic.png')
