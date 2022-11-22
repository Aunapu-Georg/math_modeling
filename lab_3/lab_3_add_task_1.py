from random import randint
import numpy as np

col = 5
row = 4

a = np.zeros((row, col))
b = np.zeros((row, col))
c = np.zeros((row, col))

for current_row in range(row):
  for current_col in range(col):
    a[current_row, current_col] = randint(-100, 100)
    b[current_row, current_col] = randint(-100, 100)
    c[current_row, current_col] = max(a[current_row, current_col],
                                      b[current_row, current_col])

print(a, end='\n\n')
print(b, end='\n\n')
print(c)
