import numpy as np

def multiplication(numbers, result = 1):

  for element in numbers:
    result *= element

  return result

numbers = np.array([3, 4, -5])
print(multiplication(numbers))
