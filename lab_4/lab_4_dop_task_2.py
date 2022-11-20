def fib(n):
  a = 0
  b = 1

  for i in range(n - 2):
    if i % 2 == 0:
      a += b
    else:
      b += a

  return(max(a, b))

print(fib(5))
print(fib(14))
