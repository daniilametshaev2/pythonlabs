import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 400)

plt.figure(figsize=(10, 6))
plt.title('Полиномы Лежандра')

# Цвета для разных степеней
colors = plt.cm.viridis(np.linspace(0, 1, 7))

# Проходим по степеням от 1 до 7
for n in range(1, 8):
    Pn = legendre(n)
    y = Pn(x)
    plt.plot(x, y, label=f'- n = {n}', color=colors[n-1])


plt.legend(title='Степень n', loc='upper right')

plt.grid(True)
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.show()
