import matplotlib.pyplot as plt
import numpy as np

def cir_ell_plotter(xa, xb, N, title, kind=None, *coefficients):
    """
    Строит круги и эллипсы
    На вход берет начало и конец графика, количество его точек, название, тип графика и его коэфиициенты
    """
    x = np.linspace(xa, xb, N)
    y = np.linspace(xa, xb, N)
    X, Y = np.meshgrid(x, y)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title(title)
    plt.axis('equal')

    if kind is None:
        print('Тип функции не задан')
    elif kind == 'circle':
        fxy = X ** 2 + Y ** 2 - coefficients[0] ** 2
        plt.contour(X, Y, fxy, levels=[coefficients[1]])
        plt.savefig('pic.png')
    elif kind == 'ellipse':
        fxy = X ** 2 / coefficients[0] ** 2 + Y ** 2 / coefficients[1] ** 2 - 1
        plt.contour(X, Y, fxy, levels=[coefficients[2]])
        plt.savefig('pic.png')
    else:
         print('Невозможно построение графика заданной функции')

"""
coefficients = [5.27, 9]
cir_ell_plotter(-11.111, 13.89, 36, 'Circle', 'circle', *coefficients)
"""

coefficients = [-12, 0.04, 3]
cir_ell_plotter(-99, 98.9, 228, 'Ellipse', 'ellipse', *coefficients)
