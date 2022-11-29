import matplotlib.pyplot as plt
import numpy as np

def par_hyp_plotter(xa, xb, N, title, kind=None, *coefficients):
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
        for current_x in x:
            y.append(coefficients[0] * current_x ** 2 + coefficients[1] * current_x + coefficients[2])
        y = np.array(y)
        plt.plot(x, y)
        plt.savefig('pic.png')
    elif kind == 'hyperbola':
        for current_x in x:
            if current_x != 0:
                y.append(coefficients[0] / current_x * coefficients[1])
        y = np.array(y)
        plt.plot(x, y)
        plt.savefig('pic.png')
    else:
        print('Невозможно построение графика заданной функции')

""" 
coefficients = [1, -2, 1]
par_hyp_plotter(-104.5, 56.234, 99, 'Parabola', 'parabola', *coefficients)
"""

coefficients = [1, -3]
par_hyp_plotter(-25.25, 25.12, 112, 'Hyperbola', 'hyperbola', *coefficients)
