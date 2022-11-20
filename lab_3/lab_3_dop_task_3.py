import numpy as np

row = 4
col = 3

mas = np.random.randint(-100, 100, size = (row, col))
maximums = []

for i in range(col):

  maximums.append(max(mas[:, i]))

print(mas, maximums, sep='\n\n')
