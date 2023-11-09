import numpy as np
matrix = np.random.randint(-20, 21, size=(5, 5))
print("Сгенерированная матрица:")
main_diagonal = np.sum(np.diagonal(matrix))
print("Значения главной диагонали:", main_diagonal)
reverse_diagonal = np.sum(np.diagonal(np.fliplr(matrix)))
print("Значения побочной диагонали:", reverse_diagonal)
