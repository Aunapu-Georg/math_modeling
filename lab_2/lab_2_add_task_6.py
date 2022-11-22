gregorian_date = input().split('.')
for index in range(len(gregorian_date)):
  gregorian_date[index] = int(gregorian_date[index])
  
olympic_date = [1, 7, -776]

olympics_after = (gregorian_date[2] - olympic_date[2]) // 4
remainder = (gregorian_date[2] - olympic_date[2]) % 4

if remainder == 0:
  if gregorian_date[1] > olympic_date[1] or gregorian_date[0] > olympic_date[0] and gregorian_date[1] == olympic_date[1]:
    print(f'OL {olympics_after}.0')
  else:
    print(f'OL {olympics_after - 1}.0')
else:
  print(f'OL {olympics_after}.{remainder}')
    