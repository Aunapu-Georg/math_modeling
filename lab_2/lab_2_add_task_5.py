from lab_2_add_task_4 import number_dividers_solver

perfect_numbers = [] 

last_number = int(input())
for number in range(4, last_number + 1):
  if sum(number_dividers_solver(number)) == number:
    perfect_numbers.append(number)

print(perfect_numbers)
