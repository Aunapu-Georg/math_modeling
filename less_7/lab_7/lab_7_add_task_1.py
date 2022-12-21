import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r', markersize=5)
trajectory, = plt.plot([], [], '--', color='g')
wheel, = plt.plot([], [], '-', color='b')

R = 3
kind = 'cycloid'

edge = 30
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.axis('equal')
ax.set_xlim(-edge, edge)

def figure_move(t, kind, circle=False):
    if circle:
        if kind == 'cycloid':
            x0 = 0
            y0 = R
            vx0 = R

            xc = x0 + vx0 * t
            yc = y0

            alpha = np.arange(0, 2 * np.pi, 0.1)
            x = xc + R * np.cos(alpha)
            y = yc + R * np.sin(alpha)
            return x, y
        elif kind == 'astroid':
            print('Надо сделать астроиду')
    elif kind == 'cycloid':
        x = R * (t - np.sin(t))
        y = R * (1 - np.cos(t))
        return x, y
    elif kind == 'astroid':
        x = R * np.cos(t) ** 3
        y = R * np.sin(t) ** 3
        return x, y

X, Y = [], []

def cycloid_animate(time):
    '''
    Вставляет координаты гифки-кружка, движущегося по циклоиде, в кортеж
    На вход берет момент времени
    '''
    current_coordinates = figure_move(time, 'cycloid')
    X.append(current_coordinates[0])
    Y.append(current_coordinates[1])

    ball.set_data(figure_move(time, 'cycloid'))
    trajectory.set_data(X, Y)

    wheel.set_data(figure_move(time, 'cycloid', True))

def astroid_animate(time):
    '''
    Вставляет координаты гифки-кружка, движущегося по астроиде, в кортеж
    На вход берет момент времени
    '''
    current_coordinates = figure_move(time, 'astroid')
    X.append(current_coordinates[0])
    Y.append(current_coordinates[1])

    ball.set_data(figure_move(time, 'astroid'))
    trajectory.set_data(X, Y)

    wheel.set_data(figure_move(time, 'astroid', True))

if kind == 'cycloid':
    ani = FuncAnimation(fig,
                        cycloid_animate,
                        frames=np.arange(0, 2 * np.pi, 0.1),
                        interval=30
                        )
elif kind == 'astroid':
    ani = FuncAnimation(fig,
                        astroid_animate,
                        frames=np.arange(0, 2 * np.pi, 0.1),
                        interval=30)

ani.save('ani.gif')
