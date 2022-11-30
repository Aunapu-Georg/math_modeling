import matplotlib.pyplot as plt
import numpy as np

def lissajous_curves(t_start, t_stop, t_step, amplitude_A, frequency_a, amplitude_B, frequency_b, phase = np.pi / 2):
    """
    Строит графику кривых Лиссажу
    На вход принимает амплитуды, частоты и фазу, а также начало и конец рассматриваемого промежутка на графике (и шаг)
    """
    t = np.arange(t_start, t_stop, t_step)
    x = amplitude_A * np.sin(frequency_a * t + phase)
    y = amplitude_B * np.sin(frequency_b * t)

    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Lissajous curve')
    plt.axis('equal')
    plt.plot(x, y)
    plt.savefig('pic.png')

lissajous_curves(-30, 30, 0.01, 1, 1.5, 4, 4.5)
