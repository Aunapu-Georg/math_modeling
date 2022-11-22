number = int(input())
fibonacci = [1, 1]

for i in range(number - 2):
  fibonacci.append(fibonacci[i] + fibonacci[i + 1])

print(fibonacci)  
