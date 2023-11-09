import numpy as np
field = np.zeros((10, 10), dtype=int)
mines_count = 10
for _ in range(mines_count):
    while True:
        row = np.random.randint(0, 10)
        col = np.random.randint(0, 10)
        if field[row, col] != -1:
            field[row, col] = -1
            break
print("Поле с минами:")
for i in range(10):
    for j in range(10):
        if field[i, j] == -1:
            print(' * ', end='')
        else:
            print(' 0 ', end='')
    print()

def count_adjacent_mines(row, col):
    count = 0
    for i in range(max(0, row-1), min(10, row+2)):
        for j in range(max(0, col-1), min(10, col+2)):
            if field[i, j] == -1:
                count += 1
    return count
while True:
    try:
        user_row = int(input("Введите номер строки (от 0 до 9): "))
        user_col = int(input("Введите номер столбца (от 0 до 9): "))
        if field[user_row, user_col] == -1:
            print("В этой ячейке мина!")
        else:
            adjacent_mines = count_adjacent_mines(user_row, user_col)
            print("В соседних ячейках", adjacent_mines, "мин")
        break
    except:
        print("Пожалуйста, введите корректные координаты ячейки")
