import numpy as np
matrix = np.random.randint(0, 10, size=(3, 4))
print("Сгенерированная матрица:")
print(matrix)
row_index_with_max_sum = np.argmax(np.sum(matrix, axis=1))
print("Индекс строки с наибольшей суммой значений:", row_index_with_max_sum)
