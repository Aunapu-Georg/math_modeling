import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

figure = 'heart'

fig, ax = plt.subplots()

if figure == 'butterfly':
    butterfly, = plt.plot([], [], '-.', color='g', label='Butterfly')
    euler_constant = 2.718281828

    def butterfly_move(angle_vel, time): 
        alpha = angle_vel * (np.pi / 180) * time
        x = np.sin(alpha) * (euler_constant ** (np.cos(alpha) - 2 * np.cos(4 * alpha) + np.sin(alpha / 12) ** 5))
        y = np.cos(alpha) * (euler_constant ** np.cos(alpha) - 2 * np.cos(4 * alpha) + np.sin(alpha / 12) ** 5)
        return x, y

    edge = 30
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    def butterfly_animate(i):
        butterfly.set_data(butterfly_move(angle_vel=1, time=i))
        return butterfly

    ani = FuncAnimation(fig,
                    butterfly_animate,
                    frames=180,
                    interval=30
                    )

    ani.save('ani.gif')


elif figure == 'heart':
    heart, = plt.plot([], [], ':', color='y', label='Heart')

    def heart_move(angle_vel, time):
        alpha = angle_vel * (np.pi / 180) * time
        x = 16 * np.sin(alpha) ** 3
        y = 13 * np.cos(alpha) - 5 * np.cos(2 * alpha) - 2 * np.cos(3 * alpha) - np.cos(4 * alpha)
        return x, y

    edge = 30
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    def heart_animate(i):
        heart.set_data(heart_move(angle_vel=1, time=i))
        return heart

    ani = FuncAnimation(fig,
                    heart_animate,
                    frames=180,
                    interval=30
                    )

    ani.save('ani.gif')
