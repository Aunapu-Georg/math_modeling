import numpy as np

a = np.zeros((2, 3))
print(a)

a[0, 2] = 5
print(a)

b = np.ones((3, 2))
print(b)

# ndarray ("not defined array") заполняет массив "компьютерными нулями" (минимальными числами, представляемыми компьютером)
d = np.ndarray((3, 3))
print(d)
