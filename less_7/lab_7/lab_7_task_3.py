import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def stunning_animations_maker(kind=None):
    fig, ax = plt.subplots()

    if kind is None:
        print('Тип анимации не задан')
    elif kind == 'butterfly':
        euler_constant = 2.718281828

        butterfly, = plt.plot([], [], '~', color='g', label='Butterfly')

        alpha = np.arange(0, 12 * np.pi, 0.1)
        x = np.sin(alpha) * (euler_constant ** (np.cos(alpha) - 2 * np.cos(4 * alpha) + np.sin(alpha / 12) ** 5))
        y = np.cis(alpha) * (euler_constant ** np.cos(alpha) - 2 * np.cos(4 * alpha) + np.sin(alpha / 12) ** 5)

        plt.axis('equal')
        edge = 5
        ax.set_xlim(-edge, edge)
        ax.set_ylim(-edge, edge)
    elif kind == 'heart':
        heart, = plt.plot([], [], '*', color='y', label='heart')

        alpha = np.arange(0, 2 * np.pi, 0.1)
        x = 16 * np.sin(alpha) ** 3
        y = 13 * np.cos(alpha) - 5 * np.cos(2 * alpha) - 2 * np.cos(3 * alpha) - np.cos(4 * alpha)

        plt.axis('equal')
        edge = 20
        ax.set_xlim(-edge, edge)
        ax.set_ylim(-edge, edge)
    else:
        print('Невозможно создание анимации заданного типа')
    
    

"""
stunning_animations_maker('butterfly')
"""

stunning_animations_maker('heart')
