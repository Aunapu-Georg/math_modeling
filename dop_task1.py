from random import randint
import numpy as np

k = 5
n = 4

a = np.zeros((n, k))
b = np.zeros((n, k))
c = np.zeros((n, k))

for i in range(n):

  for j in range(k):

    a[i, j] = randint(-100, 100)
    b[i, j] = randint(-100, 100)
    c[i, j] = max(a[i, j], b[i, j])

print(a, end='\n\n')
print(b, end='\n\n')
print(c)
