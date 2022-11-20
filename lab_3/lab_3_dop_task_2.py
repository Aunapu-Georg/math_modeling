import numpy as np
from random import randint

el = 5
mas = np.zeros(el)

for i in range(el - 1):
  mas[i] = randint(-100, 100)

print(mas, end='\n\n')

new = randint(1000, 10000)
ind = randint(0, el - 1)
print(new, ind, end='\n\n')

temp = mas[ind]
mas[ind] = new

for j in range(ind + 1, el):
  mas[j], temp = temp, mas[j]

print(mas)
      