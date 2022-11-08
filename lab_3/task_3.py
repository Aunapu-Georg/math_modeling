from task1 import earth_accel
import numpy as np

x0 = 5
y0 = 10
v = 5
alpha = 30 * np.pi
v0x = v * np.cos(alpha)
v0y = v * np.sin(alpha)

t = np.arange(0, 5, 0.01)
x = x0 + v0x * t
y = y0 * v0y * t - earth_accel * t ** 2 / 2

coords = np.zeros((len(t), 3))
for i in range(len(t)):

  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]

print(coords)
