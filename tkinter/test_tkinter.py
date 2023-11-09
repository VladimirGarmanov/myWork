from tkinter import *
from random import *
import math

win = Tk()
w = 800
h = 800
c = Canvas(width=w, height=h)
c.pack()
c1=c.create_oval(35+300,320-300,65+300,350-300,fill='white')
c2=c.create_oval(25+300,350-300,75+300,400-300,fill='white')
c3=c.create_oval(0+300,400-300,100+300,500-300,fill='white')
h1=c.create_rectangle(35+300,330-300,65+300,300-300,fill='grey')
f2=c.create_line(40+300,335-300,45+300,335-300,fill='red')
f3=c.create_line(55+300,335-300,60+300,335-300,fill='red')
colors = ['pink','blue','red','yellow','lightgreen']
sy = 5
boards = []
for i in range(5):
    x = -30
    y = randint(25,h-25)
    num = randint(0,4)
    board = c.create_rectangle(x-30,y-15,x+30,y+15,fill = colors[num])
    boards.append(board)
sx_list = []
sy_list = []
for i in range(5):
    sx = 5
    sy = 0
    sx_list.append(sx)
    sy_list.append(sy)
def animate():
    global sy

    c.move(c1,0,sy)
    c.move(c2,0,sy)
    c.move(c3, 0, sy)
    c.move(h1, 0, sy)
    c.move(f2, 0, sy)
    c.move(f3, 0, sy)
    x11,y11,x21,y21 = c.coords(h1)
    x12,y12,x22,y22 = c.coords(c1)
    x13,y13,x23,y23 = c.coords(c2)
    x14,y14,x24,y24 = c.coords(c3)
    result1 = c.find_overlapping(x12,y12,x22,y22)
    result2 = c.find_overlapping(x11,y11,x22,y22)
    result3 = c.find_overlapping(x13,y13,x23,y23)
    result4 = c.find_overlapping(x14,y14,x24,y24)

    if y11 > h:
        c.move(c1, 0, -1000)
        c.move(c2, 0, -1000)
        c.move(c3, 0, -1000)
        c.move(h1, 0, -1000)
        c.move(f2, 0, -1000)
        c.move(f3, 0, -1000)

    sy = 5
    for i in range(5):
        c.move(boards[i],sx_list[i],sy_list[i])
        x1,y1,x2,y2 = c.coords(boards[i])
        if boards[i] in result1 or boards[i] in result2 or boards[i] in result3 or boards[i] in result4:
            sx_list[i] = 0
            sy_list[i] = 5
        if x1 > w:
            x = -30
            y = randint(25, h - 25)
            c.coords(boards[i],x-30,y-15,x+30,y+15)
        if y1 > h:
            x = -30
            y = randint(25, h - 25)
            c.coords(boards[i], x - 30, y - 15, x + 30, y + 15)
            sx_list[i] = 5
            sy_list[i] = 0


    c.after(10,animate)
animate()
win.mainloop()
