a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c 

if D < 0:
  print('Нет корней')
elif D == 0:
  print('x =', -b / 2 * a)
else:
  print('x1 =', (-b + D ** 0.5) / 2 * a, '\nx2 =', (-b - D ** 0.5) / 2 * a)
  