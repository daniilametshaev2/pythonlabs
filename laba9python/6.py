import numpy as np

a = np.arange(16).reshape(4, 4)
print("До обмена:\n", a)

a[[0, 3]] = a[[3, 0]]

print("После обмена:\n", a)
