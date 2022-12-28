import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint, uniform

# Создаём координатные плоскости для создания анимации

fig, ax = plt.subplots()

atom_coordinates = [0, 0]
atom, = plt.plot([atom_coordinates[0]], [atom_coordinates[1]], 'o', color='indianred', markersize=25)

edge = 25
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

# Создаём все данные (цвет, начальное положение, скорость) для указанного количества фотонов

amount = 100
photons = []
colours = ['tomato', 'darkorange', 'forestgreen', 'paleturquoise', 'royalblue', 'rebeccapurple']
velocities = []
for current_photon in range(amount):   
        colour_index = randint(0, len(colours) - 1)
        photon, = plt.plot([], [], 'o', color=colours[colour_index], markersize=5)
        photons.append(photon)
        velocity = [randint(-10, 10), randint(-10, 10)]
        velocities.append(velocity)

def photon_move(time, vx, vy, x0, y0):
    ''' 
    Функция для вычисления координат фотонов во время движения
    В качестве аргументов подаются время, начальные скорости по осям x и y, а также координаты вылета
    '''
    current_x = x0 + vx * time
    current_y = y0 + vy * time
    return current_x, current_y

def photon_animate(time):
    '''
    Функция для подстановки координат движения фотонов для их дальнейшей анимации
    В качестве аргумента принимается время
    '''
    for current_photon in range(amount):
        photons[current_photon].set_data(photon_move(time, velocities[current_photon][0], velocities[current_photon][1], 
        start_coordinates[current_photon][0], start_coordinates[current_photon][1]))

# Создаём анимацию ранее созданных фотонов

ani = FuncAnimation(fig,
                    photon_animate,
                    frames = np.arange(0, 20, 0.1),
                    interval=30
                    )

# Сохраняем полученную анимация в формате GIF

ani.save('ani.gif')
