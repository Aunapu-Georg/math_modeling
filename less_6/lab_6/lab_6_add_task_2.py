import matplotlib.pyplot as plt
import numpy as np

def polar_ellipse(eccentricity, focal_parameter):
    """
    Строит эллипс через полярные координаты
    На вход принимает эксцентриситет и фокальный параметр
    """
    alpha = np.arange(0, 8, 0.01)
    r = focal_parameter / (1 + eccentricity *  np.cos(alpha))
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Ellipse')
    plt.axis('equal')
    plt.plot(r * np.cos(alpha), r * np.sin(alpha))
    plt.savefig('pic.png')

polar_ellipse(0.5, 4.24)
