import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Функция для получения координат фигуры Лисажу с вращением
def get_lyashu_coords(a, b, theta_rotation=0):
    t = np.linspace(0, 2*np.pi, 400)
    x = a * np.cos(t)
    y = b * np.sin(t)
    
    x_rot = x * np.cos(theta_rotation) - y * np.sin(theta_rotation)
    y_rot = x * np.sin(theta_rotation) + y * np.cos(theta_rotation)
    return x_rot, y_rot

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_title('Вращение фигуры Лисажу при изменении соотношения частот')

# Объект линии для обновления
line, = ax.plot([], [], lw=2)

# Количество кадров анимации
frames = 100

def init():
    line.set_data([], [])
    return line,

def update(frame):
    # Соотношение частот от 0 до 1
    ratio = frame / (frames - 1)
    
    a = 1 + ratio  # от 1 до 2
    b = 1 + (1 - ratio)  # от 2 до 1

    angle = ratio * 2*np.pi
    
    x, y = get_lyashu_coords(a, b, theta_rotation=angle)
    
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=frames, init_func=init,
                    blit=True, interval=50)

plt.show()
