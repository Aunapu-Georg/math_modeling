import numpy as np

from task1 import earth_accel

h = 100
alpha = np.pi / 3
beta = np.pi / 6

a = earth_accel * h * ((np.tan(beta)) ** 2)
b = 2 * ((np.cos(alpha)) ** 2) * (1 - np.tan(beta) * np.tan(alpha))
V = np.sqrt(a / b)

print(V)

from numpy import sqrt
from task1 import bolzman_const
from task1 import eiler_number
from task1 import plank_const

T = 200
E = 300

a = plank_const / sqrt((bolzman_const * T) ** 3)
b = eiler_number ** (eiler_number * -1 / bolzman_const * T)
N = (2 / sqrt(np.pi)) * a * b * sqrt(eiler_number ** T) 

print(N)
