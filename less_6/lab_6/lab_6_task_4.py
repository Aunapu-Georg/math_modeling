import matplotlib.pyplot as plt
import numpy as np

def polar_coord(coefficients, kind=None):
    """
    Строит различные графики уравнения для полярой системы координат
    На вход берет тип графика и его коэффициенты
    """
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Graph')
    plt.axis('equal')

    if kind is None:
        print('Тип функции не задан')
    elif kind == 'logarithmic_spiral':
        alpha = np.linspace(0, 8 * np.pi, 337)
        b = coefficients[0]
        r = np.exp(b * alpha)
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic.png')
    elif kind == 'archimedean_spiral':
        alpha = np.arange(0, 8, 0.01)
        k = coefficients[0]
        r = k * alpha
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic.png')
    elif kind == 'wand':
        alpha = np.arange(0.01, 8, 0.01)
        k = coefficients[0]
        r = k / np.sqrt(alpha)
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic.png')
    elif kind == 'rose':
        alpha = np.arange(0, 8, 0.01)
        k = coefficients[0]
        r = np.sin(k * alpha)
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic.png')
    else:
        print('Невозможно построение графика заданной функции')

"""
coefficients = [0.1]
polar_coord(coefficients, 'logarithmic_spiral')

coefficients = [2.0345]
polar_coord(coefficients, 'archimedean_spiral')

coefficients = [1.12]
polar_coord(coefficients, 'wand')
"""
coefficients = [8]
polar_coord(coefficients, 'rose')
