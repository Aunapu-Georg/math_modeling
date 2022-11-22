number = int(input())
reversed_number = 0
 
while number > 0:
    digit = number % 10
    number = number // 10
    reversed_number *= 10
    reversed_number += digit
 
print(reversed_number)
