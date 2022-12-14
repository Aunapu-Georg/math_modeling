import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r', markersize=5)

R = 3
kind = 'cycloid'

edge = 30
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.axis('equal')
ax.set_xlim(-edge, edge)

x = []
y = []

def figure_move(t, kind):
    if kind == 'cycloid':
        x0 = vx0 * time
        y0 = vy0
        x = R * (t - np.sin(t))
        y = R * (1 - np.cos(t))
        return x, y
    elif kind == 'astroid':
        x = R * np.cos(t) ** 3
        y = R * np.sin(t) ** 3
        return x, y

def cycloid_animate(time):
    '''
    Вставляет координаты гифки-кружка, движущегося по циклоиде, в кортеж
    На вход берет момент времени
    '''
    current_coordinates = figure_move(time, 'cycloid')
    x.append(current_coordinates[0])
    y.append(current_coordinates[1])
    ball.set_data(x, y)

def astroid_animate(time):
    '''
    Вставляет координаты гифки-кружка, движущегося по астроиде, в кортеж
    На вход берет момент времени
    '''
    current_coordinates = figure_move(time, 'astroid')
    x.append(current_coordinates[0])
    y.append(current_coordinates[1])
    ball.set_data(x, y)

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
                        interval=30
                        

ani.save('ani.gif')
