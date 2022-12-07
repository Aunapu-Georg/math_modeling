import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации

xdata, ydata = [], [] # Координаты объекта анимации

ax.set_xlim(0, 2 * np.pi) # Предел изменения переменной x
ax.set_ylim(-1, 1) # Предел изменения переменной y\

def update(frame): # Функция подстановки кооррдинат в объект анимации
    xdata.append(frame) # Расчет координаты X
    ydata.append(np.sin(frame)) # Расчет координаты Y
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,

ani = FuncAnimation(fig, # Стандартный вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames = np.arange(0, 2 * np.pi, 0.1),
                    interval = 100 # Интревал между кадрами,
                    )              # по умолчанию 200 миллисекунд

ani.save('ani.gif')
