import numpy as np
import matplotlib.pyplot as plt

# Функция для построения фигуры Лисажу
def plot_lyashu(a, b, ax, label):
    # Создаем массив углов
    theta = np.linspace(0, 2*np.pi, 400)
    # Параметризация эллипса
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    ax.plot(x, y, label=label)

# Создаем фигуру и ось
fig, ax = plt.subplots(figsize=(8,8))
ax.set_title('Фигуры Лисажу с разными соотношениями частот')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')  

# Соотношения частот
ratios = [('3:2', 3, 2),
          ('3:4', 3, 4),
          ('5:4', 5, 4),
          ('5:6', 5, 6)]

colors = ['blue', 'green', 'red', 'purple']

for i, (label_ratio, a_ratio, b_ratio) in enumerate(ratios):
    scale = 1.5
    a = a_ratio * scale
    b = b_ratio * scale
    plot_lyashu(a, b, ax, label=f'{label_ratio}')

ax.legend()
plt.grid(True)
plt.show()
