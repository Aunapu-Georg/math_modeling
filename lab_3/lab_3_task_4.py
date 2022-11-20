import numpy as np

N = 10
M = 10
k = 5

A = np.zeros((k, k))

for i in range(1, k):
  for j in range(1, k):
    a = np.sin(N * i + M * j)
    if a > 0:
      A[i][j] = a

print(A, end='\n\n')
