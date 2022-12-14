import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

dots, = plt.plot([], [], 'o', color='b', label='Dots')

edge = 1
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.axis('equal')

def dots_move(x0, y0, C=0.3, D=0.33):
    '''
    Рассчет координат точек фрактального множества
    На вход принимает координаты предыдущей функции и две константы
    '''
    x = x0 ** 2 - y0 ** 2 + C
    y = 2 * x0 * y0 + D
    return x, y

x0 = 0.1
y0 = 0.1
x = [x0]
y = [y0]

def figure_animate(time):
    '''
    Вставляет координаты точки в кортеж
    На вход берет момент времени (номер текущей точки)
    '''
    current_coordinates = dots_move(x[time - 1], y[time - 1])
    x.append(current_coordinates[0])
    y.append(current_coordinates[1])
    if time == 1:
        x[0] = current_coordinates[0]
        y[0] = current_coordinates[1]
    dots.set_data(x, y)

n = 57

ani = animation.FuncAnimation(fig,
                            figure_animate,
                            frames=np.arange(1, n),
                            interval=30
                            )  

ani.save('ani.gif')
