import matplotlib.pyplot as plt
import numpy as np

def cir_ell_plotter(xa, xb, N, title, coefficients, kind=None):
    """
    Строит круги и эллипсы
    На вход берет начало и конец графика, количество его точек, название, тип графика и его коэфиициенты
    """
    x = np.linspace(xa, xb, N)
    y = np.linspace(xa, xb, N)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title(title)
    plt.axis('equal')
    X, Y = np.meshgrid(x, y)

    if kind is None:
        print('Тип функции не задан')
    elif kind == 'circle':
        fxy = (X - coefficients[1]) ** 2 + (Y - coefficients[2]) ** 2 - coefficients[0] ** 2
        plt.contour(X, Y, fxy, levels=[0])
        plt.savefig('pic.png')
    elif kind == 'ellipse':
        fxy = (X - coefficients[2]) ** 2 / coefficients[0] ** 2 + (Y - coefficients[3]) ** 2 / coefficients[1] ** 2 - 1
        plt.contour(X, Y, fxy, levels=[0])
        plt.savefig('pic.png')
    else:
         print('Невозможно построение графика заданной функции')

"""
coefficients = [5.27, -6.24, 23.0001]
cir_ell_plotter(-111.111, 130.89, 360, 'Circle', coefficients, 'circle')
"""

coefficients = [12.9876, -4.0988, 22.43, -0.00001]
cir_ell_plotter(-99, 98.9, 228, 'Ellipse', coefficients, 'ellipse')
