import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a=1, b=1, c=0, title='Parabola plotter'):
    """ Рисователь парабол общего вида
        На входе нужно указать коэффициенты уравнения парабол
    """

    x = np.arange(-10, 10, 0.01)
    y = a * x ** 2 + b * x + c

    plt.plot(x, y, label='my parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)

    # Аналог: plt.axis('equal')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)   
    plt.legend()
    plt.savefig('pic.png')

parabola_plotter()
