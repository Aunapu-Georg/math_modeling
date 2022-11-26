import matplotlib.pyplot as plt
import numpy as np

def function_plotter(xa, xb, N, title, type=None, *coefficients):
    """
    Строит график линейной или квадратичной функции
    На вход берет начало и конец графика, количество точек для построения, навзание, тип функции и ее коэффициенты
    """
    x = np.linspace(xa, xb, N)
    y = []
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title(title)

    if type is None:
        print('Функция не задана')
    elif type == 'parabola':
        for current_x in x:
            y.append(coefficients[0] * current_x ** 2 + coefficients[1] * current_x + coefficients[2])
        y = np.array(y)
        plt.plot(x, y)
        plt.savefig('pic.png')
    elif type == 'line':
        for current_x in x:
            y.append(coefficients[0] * current_x + coefficients[1])
        y = np.array(y)
        plt.plot(x, y')
        plt.savefig('pic.png')
    else:
        print('Невозможно построение графика заданной функции')

coefficients = [1, -2, 1]
function_plotter(-104.5, 56.234, 99, 'Parabola', 'parabola', *coefficients)
