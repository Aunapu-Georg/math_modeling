a = float(input())
b = float(input())
c = float(input())

if a + b > c and b + c > a and a + c > b:
  print('Существует')
  if a == b == c:
    print('Равносторонний')
  elif a == b or b == c or a == c:
    print('Равнобедренный')
  else:
    print('Рахносторонний')
else:
  print('Не существует')
