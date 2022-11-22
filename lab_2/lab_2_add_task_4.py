number = int(input())
number_dividers = []
prime_numbers = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
                 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
current = 0

while number != 1:
  while number % prime_numbers[current] == 0:
    number = number // prime_numbers[current]
    number_dividers.append(prime_numbers[current])
  current += 1

print(number_dividers)
