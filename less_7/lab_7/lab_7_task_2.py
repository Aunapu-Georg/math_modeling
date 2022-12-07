import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
circle, = plt.plot([], [], 'o', color='b', label='Circle')

def circle_move(k, time):
    R = k * time
    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = R  * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

edge = 100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    circle.set_data(circle_move(1.1, i))
    return circle

ani = animation.FuncAnimation(fig,
                              animate, 
                              frames=100, 
                              interval=30)

ani.save('ani.gif')
