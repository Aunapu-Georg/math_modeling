import matplotlib.pyplot as plt
import numpy as np

def stair_function(stairs_amount, stair_lenght, stair_height, x_start):
    """
    Строит график функции "лесенки"
    На вход принимает количество "ступенек", начало графика, а также длину ступени
    """
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Stair function')
    plt.axis('equal')
    for current_stair in range(stairs_amount):
        x_position = x_start + current_stair * stair_lenght
        x_end = x_position + stair_lenght
        x = np.linspace(x_position, x_end, 2)
        y_position = stair_height * (stairs_amount - current_stair)
        y = np.full(2, y_position)
        plt.plot(x, y)
    plt.savefig('pic.png')

stair_function(16, 1.56, 1.01, -14.01, 23.51)
