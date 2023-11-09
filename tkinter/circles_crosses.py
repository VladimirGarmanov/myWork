from tkinter import *
from random import *

root = Tk()
W = 600
H = 600



c = Canvas(root, width=W, height=H)
c.pack()
c_o = 0
x = 100
y = 100
for i in range(4):
    c.create_line(x,y,x+300,y)
    y += 100
x = 100
y = 100
for i in range(4):
    c.create_line(x,y,x,y+300)
    x += 100
coords = []
def move_mouse(event):
    global  a,c_o
    r = 15
    num = 0
    x, y = event.x, event.y  # even = метод считывает координаты мышки'
    if c_o%2 == 0:
        cx = 100
        cy = 100
        for i in range(3):
            if cx < x < cx+100:
                for k in range(3):
                    if cy <y<cy+100:
                        for h in range(len(coords)):
                            if h%2 == 0:
                                if cx == coords[h] and cy == coords[h+1]:
                                    print(cx,cy,coords[h],coords[h+1])
                                    print('Здесь нельзя строить')
                                    num = 1
                        if num == 0:
                            c.create_oval(cx, cy, cx + 100, cy + 100, fill='blue')
                            c_o += 1
                        if num == 1:
                            num = 0

                        if len(coords) == 0:
                            c.create_oval(cx, cy, cx + 100, cy + 100, fill='blue')
                            c_o += 1


                        coords.append(cx)
                        coords.append(cy)
                        print(cx,cy)
                    cy += 100
            cx+=100


    else:
        cx = 100
        cy = 100
        for i in range(3):
            if cx < x < cx + 100:
                for k in range(3):
                    if cy < y < cy + 100:
                        for h in range(len(coords)):
                            if h % 2 == 0:
                                if cx == coords[h] and cy == coords[h+1]:
                                    print('Здесь нельзя строить')
                                    num = 1
                        if num == 0:
                            c.create_line(cx, cy, cx + 100, cy + 100, fill='red')
                            c.create_line(cx + 100, cy, cx, cy + 100, fill='red')
                            c_o += 1
                        if num == 1:
                            num = 0

                        if len(coords) == 0:
                            c.create_line(cx, cy, cx + 100, cy + 100, fill='red')
                            c.create_line(cx + 100, cy, cx, cy + 100, fill='red')
                            c_o += 1


                        coords.append(cx)
                        coords.append(cy)

                        print(cx, cy)
                    cy += 100
            cx += 100



c.bind('<Button-1>', move_mouse)
root.mainloop()