from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.geometry('600x600')
area = [[], [], []]
turn = 1


def new_game():
    global turn
    turn = 1
    for i in area:
        for j in range(3):
            i[j]['text'] = ''
            i[j].configure(bg='white')


def won():
    if area[0][0]['text'] == 'x' and area[0][1]['text'] == 'x' and area[0][2]['text'] == 'x':
        return 'x'
    if area[1][0]['text'] == 'x' and area[1][1]['text'] == 'x' and area[1][2]['text'] == 'x':
        return 'x'
    if area[2][0]['text'] == 'x' and area[2][1]['text'] == 'x' and area[2][2]['text'] == 'x':
        return 'x'
    if area[0][0]['text'] == 'x' and area[1][0]['text'] == 'x' and area[2][0]['text'] == 'x':
        return 'x'
    if area[0][1]['text'] == 'x' and area[1][1]['text'] == 'x' and area[2][1]['text'] == 'x':
        return 'x'
    if area[0][2]['text'] == 'x' and area[1][2]['text'] == 'x' and area[2][2]['text'] == 'x':
        return 'x'
    if area[0][0]['text'] == 'x' and area[1][1]['text'] == 'x' and area[2][2]['text'] == 'x':
        return 'x'
    if area[0][2]['text'] == 'x' and area[1][1]['text'] == 'x' and area[2][0]['text'] == 'x':
        return 'x'

    if area[0][0]['text'] == 'o' and area[0][1]['text'] == 'o' and area[0][2]['text'] == 'o':
        return 'o'
    if area[1][0]['text'] == 'o' and area[1][1]['text'] == 'o' and area[1][2]['text'] == 'o':
        return 'o'
    if area[2][0]['text'] == 'o' and area[2][1]['text'] == 'o' and area[2][2]['text'] == 'o':
        return 'o'
    if area[0][0]['text'] == 'o' and area[1][0]['text'] == 'o' and area[2][0]['text'] == 'o':
        return 'o'
    if area[0][1]['text'] == 'o' and area[1][1]['text'] == 'o' and area[2][1]['text'] == 'o':
        return 'o'
    if area[0][2]['text'] == 'o' and area[1][2]['text'] == 'o' and area[2][2]['text'] == 'o':
        return 'o'
    if area[0][0]['text'] == 'o' and area[1][1]['text'] == 'o' and area[2][2]['text'] == 'o':
        return 'o'
    if area[0][2]['text'] == 'o' and area[1][1]['text'] == 'o' and area[2][0]['text'] == 'o':
        return 'o'


def press(but):
    global turn
    if but['text'] == '':
        if turn % 2 == 1:
            but['text'] = 'x'
            but.configure(bg='red')
            msg = "Ходят нолики"
            showinfo('Оповещатель', msg)
        if turn % 2 == 0:
            but['text'] = 'o'
            but.configure(bg='blue')
            msg = "Ходят крестики"
            showinfo('Оповещатель', msg)
        turn += 1
        if won() == 'x':
            msg = "Крестики победили"
            showinfo('Оповещатель', msg)
            new_game()
        elif won() == 'o':
            msg = "Нолики победили"
            showinfo('Оповещатель', msg)
            new_game()
        elif turn == 10:
            msg = "Ничья"
            showinfo('Оповещатель', msg)
            new_game()



    else:
        msg = "ОШИБКА"
        showinfo('Оповещатель', msg)


for i in range(3):
    for j in range(3):
        but1 = Button(window, text='', width=12, height=6, font=('Verdana', 20))
        area[i].append(but1)
        but1.place(x=i * 200, y=j * 200)
        but1['command'] = lambda but=but1: press(but)

window.mainloop()