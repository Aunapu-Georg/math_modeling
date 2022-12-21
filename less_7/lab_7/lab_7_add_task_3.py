import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
star, = plt.plot([], [], '-.', color='c')

edge = 25
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

alpha =  np.arange(0, 4.1 * np.pi, 0.1)
x1 = 12 * np.cos(alpha) + 8 * np.cos(1.5 * alpha)
y1 = 12 * np.sin(alpha) - 8 * np.sin(1.5 * alpha)

def star_move(time):
    x2 = x1 * np.cos(time) - y1 * np.sin(time)
    y2 = y1 * np.cos(time) + x1 * np.sin(time)
    return x2, y2

def star_animate(time):
    star.set_data(star_move(time))
    return star

ani = FuncAnimation(fig,
                    star_animate,
                    frames = np.arange(0, 4.1 * np.pi, 0.1),
                    interval=30
                    )

ani.save('ani.gif')
