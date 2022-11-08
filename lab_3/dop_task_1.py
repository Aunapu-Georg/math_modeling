from random import randint
import numpy as np

col = 5
row = 4

a = np.zeros((row, col))
b = np.zeros((row, col))
c = np.zeros((row, col))

for i in range(row):

  for j in range(col):

    a[row, col] = randint(-100, 100)
    b[row, col] = randint(-100, 100)
    c[row, col] = max(a[row, col], b[row, col])

print(a, end='\n\n')
print(b, end='\n\n')
print(c)
