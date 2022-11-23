import matplotlib.pyplot as plt
import numpy as np

x = [1, 1, 5, 5, 1]
y = [1, 5, 5, 1, 1]

plt.plot(x, y, marker='.', ms=10)
plt.savefig('pic.png')
