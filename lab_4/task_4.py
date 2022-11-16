import numpy as np

def y(a, b, n):

  x = np.linspace(a, b, n)
  return x ** 2

print(y(-10, 10, 50))
