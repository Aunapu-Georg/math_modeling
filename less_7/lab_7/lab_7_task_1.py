import matplotlib.pyplot as plt
import numpy as np

def cycloid_astroid_plotter(R, kind=None):
    alpha = np.arange(0, 2 * np.pi, 0.01)
    if kind is None:
        print('Тип функции не задан')
    elif kind == 'cycloid':
        x = R * (alpha - np.sin(alpha))
        y = R * (1 - np.cos(alpha))
        plt.plot(x, y, ls='-', lw=4)
        plt.savefig('pic.png')
    elif kind == 'astroid':
        x = R * np.cos(alpha) ** 3
        y = R * np.sin(alpha) ** 3
        plt.plot(x, y, ls='--', lw=2)
        plt.savefig('pic.png')
    else:
        print('Невозможно построение графика функции заданного типа')

"""
cycloid_astroid_plotter(4.5, 'cycloid')
"""

cycloid_astroid_plotter(3, 'astroid')
