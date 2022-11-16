import numpy as np

def mult(mas):
  
  res = 1

  for el in mas:

    res *= el

  return res

num = np.array([3, 4, -5])

print(mult(num))
