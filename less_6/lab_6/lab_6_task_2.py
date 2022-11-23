import matplotlib.pyplot as plt
import numpy as np

def function_plotter(xa, xb, N, title, type = None, *args):
    x = np.linspace(xa, xb, N)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title(title)

    if type == None:
        print('Функция не задана')
    elif type == 'parabola':
        y = args[0] * x ** 2 + args[1] * x + args[2]
        plt.plot(x, y, label='graphic')
        plt.savefig('pic.png')
    elif type == 'line':
        y = args[0] * x + args[1]
        plt.plot(x, y, label='graphic')
        plt.savefig('pic.png')
    else:
        print('Невозможно построение графика заданной функции')

arguments = np.array([1, -2, 1])
function_plotter(-104.5, 56.234, 99, 'Parabola', 'parabola', arguments)
