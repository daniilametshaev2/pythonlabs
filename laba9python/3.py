import numpy as np
array = np.random.randn(10, 4)

min_value = np.min(array)
max_value = np.max(array)
mean_value = np.mean(array)
std_dev = np.std(array)
first_five_rows = array[:5]

print("Массив:\n", array)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_dev)
print("Первые 5 строк массива:\n", first_five_rows)
