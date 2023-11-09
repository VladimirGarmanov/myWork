import numpy as np
matrix = np.random.randint(10, 100, size=(5, 5))
print("Сгенерированная матрица:")
print(matrix)
max_value = np.max(matrix)
min_value = np.min(matrix)
print("Максимальное число:", max_value)
print("Минимальное число:", min_value)