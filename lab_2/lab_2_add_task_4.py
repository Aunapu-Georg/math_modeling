from lab_2_prime_numbers_solver import prime_numbers_solver

def number_dividers_solver(number:int = 0): # Находит простые делители числа, а не все возможные уникальные делители, так что не подходит для использования в 6 дополнительном задании, но все равно там использован
  number_dividers = [1]
  prime_numbers = prime_numbers_solver(1000)
  current = 0
  
  while number != 1:
    while number % prime_numbers[current] == 0:
      number = number // prime_numbers[current]
      number_dividers.append(prime_numbers[current])
    current += 1
  
  return number_dividers
