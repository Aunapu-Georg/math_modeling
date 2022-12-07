import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
circle = plt.plot([], [], 'o', color='b', label='Circle')

def circle_move(k, time):
    R = k * time
    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = R  * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

plt.axis('equal')

def animate(i):
    circle.set_data(circle_move(k=1.5, time=i))
    return circle

ani = animation.FuncAnimation(fig,
                              animate, 
                              frames=100, 
                              interval=30)

ani.save('ani.gif')
