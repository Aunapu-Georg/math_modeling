from task4 import A

B = A.copy()

A[ : , 1], A[ : , 0] = B[ : , 0], B[ : , 1]

print(A)
