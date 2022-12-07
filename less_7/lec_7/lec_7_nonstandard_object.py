import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x,  y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(0.5, 0.01, 0.01, i))
    return ball

ani = animation.FuncAnimation(fig,
                              animate, 
                              frames=100, 
                              interval=30)

ani.save('ani.gif')
