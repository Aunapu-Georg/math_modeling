import numpy as np

from task1 import earth_accel
from task1 import pi

h = 100
alpha = pi / 3
beta = pi / 6

V = np.sqrt((earth_accel * h * (np.tan(beta)) ** 2) / (2 * (np.cos(alpha) ** 2) * (1 - np.tan(beta) * np.tan(alpha))))

print(V)
