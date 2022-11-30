import matplotlib.pyplot as plt
import numpy as np

def par_hyp_plotter(xa, xb, N, title, coefficients, kind=None):
    """
    Строит график линейной или квадратичной функции
    На вход берет начало и конец графика, количество точек для построения, название, тип функции и ее коэффициенты
    """
    x = np.linspace(xa, xb, N)
    y = []
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title(title)
    plt.axis('equal')

    if kind is None:
        print('Тип функции не задан')
    elif kind == 'parabola':
        y = coefficients[0] * x ** 2 + coefficients[1] * x + coefficients[2]
        plt.plot(x, y)
        plt.savefig('pic.png')
    elif kind == 'hyperbola':
        y = np.linspace(xa, xb, N)
        X, Y  = np.meshgrid(x, y)
        fxy = X ** 2 / coefficients[0] ** 2 - Y ** 2 / coefficients[1] ** 2
        plt.contour(X, Y, fxy, levels=[0])
        plt.savefig('pic.png')
    else:
        print('Невозможно построение графика заданной функции')

"""
coefficients = [1.234, -5.625, 0.53]
par_hyp_plotter(-104.5, 106.234, 99, 'Parabola', coefficients, 'parabola')
""" 

coefficients = [4.865, -3.913]
par_hyp_plotter(-25.25, 25.12, 112, 'Hyperbola', coefficients, 'hyperbola')
