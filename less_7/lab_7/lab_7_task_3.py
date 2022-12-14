import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

x = []
y = []

kind = 'butterfly'

if kind == 'heart':
    figure, = plt.plot([], [], ':', color='y', label='Heart')

    edge = 30
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
elif kind == 'butterfly':
    figure, = plt.plot([], [], '-.', color='g', label='Butterfly')

    edge = 5
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

def figure_move(t, kind):
    '''
    Рассчитывает координаты функции гифки
    На вход берет тип гифки и время
    '''
    if kind == 'heart':
        x_current = 16 * np.sin(t) ** 3
        y_current = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
        return x_current, y_current
    elif kind == 'butterfly':
        euler_constant = 2.718281828
        x_current = np.sin(t) * (euler_constant ** np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5)
        y_current = np.cos(t) * (euler_constant ** np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5)
        return x_current, y_current

def butterfly_animate(time):
    '''
    Вставляет координаты гифки-бабочки в кортеж
    На вход берет момент времени
    '''
    current_coordinates = figure_move(time, 'butterfly')
    x.append(current_coordinates[0])
    y.append(current_coordinates[1])
    figure.set_data(x, y)

def heart_animate(time):
    '''
    Вставляет координаты гифки-бабочки в кортеж
    На вход берет момент времени
    '''
    current_coordinates = figure_move(time, 'heart')
    x.append(current_coordinates[0])
    y.append(current_coordinates[1])
    figure.set_data(x, y)

if kind == 'butterfly':
    ani = FuncAnimation(fig,
                        butterfly_animate,
                        frames=np.arange(0, 12 * np.pi, 0.1),
                        interval=30
                        )
elif kind == 'heart':
    ani = FuncAnimation(fig,
                        heart_animate,
                        frames=np.arange(0, 2 * np.pi, 0.1),
                        interval=30
                        )

ani.save('ani.gif')
