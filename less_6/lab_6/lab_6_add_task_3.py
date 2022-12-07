import matplotlib.pyplot as plt
import numpy as np

def deflection_function(a, b, x_start, x_stop, x_points):
    """
    Строит функцию с изломом в виде параболы
    На вход принимает начало и  окнец излома и самого графика, а также количество точек на каждом учатке графика
    """
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Piecewise graph')
    plt.axis('equal')

    y = np.zeros(len())

    x = np.linspace(x_start, a, 2)
    y = np.full(len(x), a ** 2)
    plt.plot(x, y)

    x = np.linspace(a, b, x_points)
    y = x ** 2
    plt.plot(x, y)

    x = np.linspace(b, x_stop, 2)
    y = np.full(len(x), b ** 2)
    plt.plot(x, y)
    
    plt.savefig('pic.png')

deflection_function(-2.67, 5.78, -11.26, 23.6, 100)
