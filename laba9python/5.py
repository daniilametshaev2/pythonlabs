import numpy as np

def logpdf_multivariate_normal(X, m, C):
    """
    Вычисление логарифма плотности многомерного нормального распределения.
    
    Параметры:
    - X: массив размером (N, D) — точки, в которых считаем плотность
    - m: вектор размером (D,) — математическое ожидание
    - C: матрица размером (D, D) — ковариационная матрица

    Возвращает:
    - logpdf: массив размером (N,) — логарифмы плотностей
    """
    N, D = X.shape
    XC = X - m  # Центрируем данные

    inv_C = np.linalg.inv(C)
    sign, logdet_C = np.linalg.slogdet(C)

    # Вычисление квадратичной формы: (x - m)^T * C^{-1} * (x - m)
    quad_form = np.sum((XC @ inv_C) * XC, axis=1)

    log_pdf = -0.5 * (D * np.log(2 * np.pi) + logdet_C + quad_form)
    return log_pdf

from scipy.stats import multivariate_normal
import time

# Пример данных
np.random.seed(42)
N, D = 10000, 5
X = np.random.randn(N, D)
m = np.random.randn(D)
A = np.random.randn(D, D)
C = A @ A.T  # Сделаем ковариационную матрицу положительно определённой

# Собственная реализация
start = time.time()
logpdf_custom = logpdf_multivariate_normal(X, m, C)
custom_time = time.time() - start

# SciPy реализация
start = time.time()
logpdf_scipy = multivariate_normal(mean=m, cov=C).logpdf(X)
scipy_time = time.time() - start

# Проверка точности
max_abs_diff = np.max(np.abs(logpdf_custom - logpdf_scipy))
print(f"Макс. абсолютное отличие: {max_abs_diff:.6e}")
print(f"Время (наша реализация): {custom_time:.4f} сек")
print(f"Время (SciPy): {scipy_time:.4f} сек")
