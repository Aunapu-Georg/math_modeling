import numpy as np

def y(start, stop, segments):
  x = np.linspace(start, stop, segments)
  return x ** 2

print(y(-10, 10, 50))
