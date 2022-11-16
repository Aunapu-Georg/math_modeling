def area_solver(*args):

  area = 0

  if args[0] == 'triangle':

    area = args[1] * args[2] * 0.5

  elif args[0] == 'square':

    area = args[1] ** 2

  else:

    area = args[1] * 3.14 * 2

  return area

print(area_solver('triangle', 15, 5))
print(area_solver('square', 7.8))
print(area_solver('circle', 756))
]