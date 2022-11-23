import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(radius=10):
    """ Рисует окружность заданного радиуса
    """

    x = np.arange(-2 * radius, 2 * radius, 0.1)
    y = np.arange(-2 * radius, 2 * radius, 0.1)

    # Переход к неявнозаданным кординатам
    X, Y = np.meshgrid(x, y)

    fxy = X ** 2 + Y ** 2 - radius ** 2 # Уравнение окружности

    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal') # Аналог: plt.xlim() и plt.ylim()
    plt.savefig('pic.png')

circle_plotter()
