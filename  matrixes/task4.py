
import numpy as np
matrix = np.random.randint(0, 26, size=(7, 7))
print("Сгенерированная матрица:")
for row in matrix:
    print("  ".join(str(elem) for elem in row))
player1_score = 0
player2_score = 0

for i in range(3):
    while True:
        try:
            row = int(input("Игрок 1, выберите строку (от 0 до 6): "))
            col = int(input("Игрок 1, выберите столбец (от 0 до 6): "))
            if matrix[row][col] != -1:
                player1_score += matrix[row][col]
                matrix[row][col] = -1  # Помечаем, что ячейка открыта
                print("У Игрока 1 теперь ", player1_score, "очков")
                break
            else:
                print("Эта ячейка уже открыта, выберите другую")
        except:
            print("Пожалуйста, введите корректные координаты")

    while True:
        try:
            row = int(input("Игрок 2, выберите строку (от 0 до 6): "))
            col = int(input("Игрок 2, выберите столбец (от 0 до 6): "))
            if matrix[row][col] != -1:
                player2_score += matrix[row][col]
                matrix[row][col] = -1
                print("У Игрока 2 теперь", player2_score, "очков")
                break
            else:
                print("Эта ячейка уже открыта, выберите другую")
        except:
            print("Пожалуйста, введите корректные координаты")
if player1_score > player2_score:
    print("Игрок 1 побеждает с", player1_score, "очками!")
elif player2_score > player1_score:
    print("Игрок 2 побеждает с", player2_score, "очками!")
else:
    print("Ничья! Оба игрока набрали по", player1_score, "очков!")
