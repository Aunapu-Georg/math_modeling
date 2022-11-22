def prime_numbers_solver(count:int = 0):
  prime_numbers = [2]
  
  actual_count = 1
  number = 3
  while actual_count < count:
    state = True
    for current_prime in prime_numbers:
      if number % current_prime == 0:
        state = False
        break
    if state:
      prime_numbers.append(number)
      actual_count += 1
    number += 1
  
  return prime_numbers
