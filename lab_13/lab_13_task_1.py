import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Определяем переменную величину
frames = 730
days_in_year = 365
years = 2
t = np.linspace(0, years*days_in_year, 730)
 
# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (xA, v_xA, yA, v_yA,
     xB, v_xB, yB, v_yB,
     xC, v_xC, yC, v_yC) = s
 
    # Динамика первого тела под влиянием второго и третьего
    dxdtA = v_xA
    dv_xdtA = (
      	    - G * mB * (xA - xB) 
               / ((xA - xB)**2 + (yA - yB)**2)**1.5
            - G * mC * (xA - xC) 
               / ((xA - xC)**2 + (yA - yC)**2)**1.5
              )
    dydtA = v_yA
    dv_ydtA = (
      	    - G * mB * (yA - yB) 
               / ((xA - xB)**2 + (yA - yB)**2)**1.5
            - G * mB * (yA - yC) 
               / ((xA - xC)**2 + (yA - yC)**2)**1.5
    	      )
 
    # Динамика второго тела под влиянием первого и третьего
    dxdtB = v_xB
    dv_xdtB = (
      	    - G * mA * (xB - xA) 
               / ((xB - xA)**2 + (yB - yA)**2)**1.5
            - G * mC * (xB - xC) 
               / ((xB - xC)**2 + (yB - yC)**2)**1.5
    	      )
    dydtB = v_yB
    dv_ydtB = (
      	    - G * mA * (yB - yA) 
               / ((xB - xA)**2 + (yB - yA)**2)**1.5
            - G * mC * (yB - yC) 
               / ((xB - xC)**2 + (yB - yC)**2)**1.5
              )
 
    # Динамика третьего тела под влиянием второго и первого
    dxdtC = v_xC
    dv_xdtC = (
      	    - G * mA * (xC - xA) 
               / ((xC - xA)**2 + (yC - yA)**2)**1.5
            - G * mB * (xC - xB) 
               / ((xC - xB)**2 + (yC - yB)**2)**1.5
              )
    dydtC = v_yC
    dv_ydtC = (
      	    - G * mA * (yC - yA) 
               / ((xC - xA)**2 + (yC - yA)**2)**1.5
            - G * mB * (yC - yB) 
               / ((xC - xB)**2 + (yC - yB)**2)**1.5
              )
 
    return (dxdtA, dv_xdtA, dydtA, dv_ydtA,
            dxdtB, dv_xdtB, dydtB, dv_ydtB,
            dxdtC, dv_xdtC, dydtC, dv_ydtC)
 
# Определяем начальные значения и параметры, 
# входящие в систему диф. уравнений

G = 6.67 * 10**(-11)
M = 1.98847 * 10 ** 30
au = 149 * 10 ** 9

mA = 1.06 * M
mB = 0.96 * M
mC = 0.67 * M

xA0 = 0
v_xA0 = 8638
yA0 = 0
v_yA0 = 0
 
xB0 = 12.3 * au
v_xB0 = 0
yB0 = 0
v_yB0 = 6000
 
xC0 = 12.97 * au
v_xC0 = 0
yC0 = 0
v_yC0 = -4000
 
s0 = (xA0, v_xA0, yA0, v_yA0,
      xB0, v_xB0, yB0, v_yB0,
      xC0, v_xC0, yC0, v_yC0)
 
# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)
 
# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()
 
balls = []
balls_lines = []
 
for i in range(3):
    balls.append(plt.plot([], [], 'o', color='b'))
    balls_lines.append(plt.plot([], [], '-', color='r'))
 
def animate(i):
    for j in range(3):
        balls[j][0].set_data(sol[i, 4*j], sol[i, 4*j+2])
        balls_lines[j][0].set_data(sol[:i, 4*j], sol[:i, 4*j+2])
 
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)
 
plt.axis('equal')
edge = 20 * au
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani.save('ani.gif')
