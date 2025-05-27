import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

# Находим индексы нулей
zero_indices = np.where(x == 0)[0]
elements_after_zero = []

for idx in zero_indices:
    if idx + 1 < len(x):
        elements_after_zero.append(x[idx + 1])

if elements_after_zero:
    max_element = max(elements_after_zero)
    print("Максимальный элемент после нуля:", max_element)
else:
    print("Нет элементов после нулей.")
