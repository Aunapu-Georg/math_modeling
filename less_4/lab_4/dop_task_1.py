def stepen(a, n):
  mnozh = a

  for i in range(abs(n) - 1):
    a *= mnozh

  if n < 0:
    return 1 / a
  else:
    return a

print(stepen(5, -6))
print(stepen(2, 10))