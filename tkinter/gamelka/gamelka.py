from tkinter import *

from random import *
root = Tk()

c = Canvas(width=800, height=800)

c.pack()

player_up = PhotoImage(file='Player_Up.png')

player_right = PhotoImage(file='Player_Right.png')

player_left = PhotoImage(file='Player_Left.png')

player_down = PhotoImage(file='Player_Down.png')

x = 100

y = 100

q = randint(1, 35)

p = randint(1, 35)

player = c.create_image(x, y, image=player_down)

d = "down"

i = 0

x_death = -100

y_death = -100

x_won = 0

y_won = 0

sx1 = -1

sy1 = -1

sx2 = -1

sy2 = -1

game_status = True


if 1 <= q <= 6:
    x1 = 50

    y1 = -100 * q + 650

if 6 <= q <= 11:
    y1 = 50

    x1 = q * 100 - 550

if 12 <= q <= 16:
    x1 = 150

    y1 = -100 * q + 1750

if 16 <= q <= 20:
    y1 = 150

    x1 = 100 * q - 1450

if 21 <= q <= 24:
    x1 = 250

    y1 = -100 * q + 2650

if 24 <= q <= 27:
    y1 = 250

    x1 = 100 * q - 2150

if 28 <= q <= 30:
    x1 = 350

    y1 = -100 * q + 3350

if 30 <= q <= 32:
    y1 = 350

    x1 = 100 * q - 2650

if 33 <= q <= 34:
    x1 = 450

    y1 = -100 * q + 3850

if 34 <= q <= 35:
    y1 = 450

    x1 = 100 * q - 2950

if 1 <= p <= 6:
    x2 = 50

    y2 = -100 * p + 650

if 6 <= p <= 11:
    y2 = 50

    x2 = p * 100 - 550

if 12 <= p <= 16:
    x2 = 150

    y2 = -100 * p + 1750

if 16 <= p <= 20:
    y2 = 150

    x2 = 100 * p - 1450

if 21 <= p <= 24:
    x2 = 250

    y2 = -100 * p + 2650

if 24 <= p <= 27:
    y2 = 250

    x2 = 100 * p - 2150

if 28 <= p <= 30:
    x2 = 350

    y2 = -200 * p + 6350

if 30 <= p <= 32:
    y2 = 350

    x2 = 100 * p - 2650

if 33 <= p <= 34:
    x2 = 450

    y2 = -100 * p + 3850

if 34 <= p <= 35:
    y2 = 450

    x2 = 100 * p - 2950

if p == 36:
    x2 = 550

    y2 = 550

if q == 36:
    x1 = 550

    y1 = 550

dyra1 = c.create_oval(x1, y1, x1 + 100, y1 + 100, fill="black")

dyra2 = c.create_oval(x2, y2, x2 + 100, y2 + 100, fill="black")


def move():
    global sx1, sy1, dyra1, dyra2, i, sx2, sy2

    c.move(dyra2, sx2, sy2)

    c.move(dyra1, sx1, sy1)

    x1, y1, x2, y2 = c.coords(dyra1)

    x3, y3, x4, y4 = c.coords(dyra2)

    result = c.find_overlapping(x, y, x + 50, y + 50)

    if dyra1 in result or dyra2 in result:
        i = 1

        x_death = x

        y_death = y

    if i == 1:
        player_death = c.create_image(x_death, y_death, image=player_down)

        c.delete(player)

        c.create_text(350, 100, text="GAME OVER FOR YOU", fill="red", font="Verdana 14")

    if x2 > 650:
        sx1 = -sx1

    if x1 < 50:
        sx1 = -sx1

    if x4 > 650:
        sx2 = -sx2

    if x3 < 50:
        sx2 = -sx2

    if y1 < 50:
        sy1 = -sy1

    if y2 > 650:
        sy1 = -sy1

    if y3 < 50:
        sy2 = -sy2

    if y4 > 650:
        sy2 = -sy2

    c.after(10, move)


def board():
    c.create_text(600, 600,
                  text="Иди сюда",
                  justify=CENTER, font="Verdana 14")
    for i in range(7):
        c.create_line(50, 50 + i * 100, 650, 50 + i * 100, fill="dark green")

    for i in range(7):
        c.create_line(50 + i * 100, 50, 50 + i * 100, 650, fill="dark green")


def change_player(direc, img):
    global d

    d = direc

    c.itemconfig(player, image=img)


def rotate(e):
    global x, y, player, dyra1, dyra2, game_status, i, x_death, y_death, x_won, y_won

    x1, y1, x2, y2 = c.coords(dyra1)

    x3, y3, x4, y4 = c.coords(dyra2)

    if (e.keysym == 'Right'):

        if (d == 'down'):

            change_player('right', player_right)

        elif (d == 'right'):

            change_player('up', player_up)

        elif (d == 'up'):

            change_player('left', player_left)

        elif (d == 'left'):

            change_player('down', player_down)

    if (e.keysym == 'Left'):

        if (d == 'down'):

            change_player('left', player_left)

        elif (d == 'left'):

            change_player('up', player_up)

        elif (d == 'up'):

            change_player('right', player_right)

        elif (d == 'right'):

            change_player('down', player_down)

    if (e.keysym == 'Up'):

        if (d == 'down'):

            y += 100

            c.delete(player)

            player = c.create_image(x, y, image=player_down)

        elif (d == 'right'):

            x += 100

            c.delete(player)

            player = c.create_image(x, y, image=player_right)

        elif (d == 'up'):

            y -= 100

            c.delete(player)

            player = c.create_image(x, y, image=player_up)

        elif (d == 'left'):

            x -= 100

            c.delete(player)

            player = c.create_image(x, y, image=player_left)

    if (e.keysym == 'Down'):

        if (d == 'down'):

            y -= 100

            c.delete(player)

            player = c.create_image(x, y, image=player_down)

        elif (d == 'right'):

            x -= 100

            c.delete(player)

            player = c.create_image(x, y, image=player_right)

        elif (d == 'up'):

            y += 100

            c.delete(player)

            player = c.create_image(x, y, image=player_up)

        elif (d == 'left'):

            x += 100

            c.delete(player)

            player = c.create_image(x, y, image=player_left)

    if 550 <= x <= 650 and 550 <= y <= 650:
        i = 2

        x_won = x

        y_won = y

    if i == 1:
        player_death = c.create_image(x_death, y_death, image=player_down)

        c.delete(player)

        c.create_text(350, 100, text="GAME OVER FOR YOU", fill="red", font="Verdana 14")

    if i == 2:
        c.delete(player)

        c.delete(dyra1)

        c.delete(dyra2)

        player_death = c.create_image(x_won, y_won, image=player_down)

        c.create_text(350, 100, text="YOU WON", fill="red", font="Verdana 14")


def game():
    move()

    board()


c.bind_all('<KeyPress-Right>', rotate)

c.bind_all('<KeyPress-Left>', rotate)

c.bind_all('<KeyPress-Up>', rotate)

c.bind_all('<KeyPress-Down>', rotate)

game()
root.mainloop()