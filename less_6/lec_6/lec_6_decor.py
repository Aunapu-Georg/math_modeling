import matplotlib.pyplot as plt
import numpy as numpy

x = [3, 4, 5]
y = [40, 10, 30]

plt.plot(x, y, color='g', label='line', marker='>', ms=5)

# --- Оформление ---
plt.xlabel('Coord: x') # Подпись оси ОХ
plt.ylabel('Coord: y') # Подпись оси ОY
plt.legend() # Вызов легенды
plt.title('Base') # Общая подпись графика
plt.grid() # Подключение сетки
plt.savefig('pic.png')
