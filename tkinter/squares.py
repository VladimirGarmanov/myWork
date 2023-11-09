from tkinter import *
from random import *
win = Tk()
w = 800
h = 800
c = Canvas(width = w, height = h)
c.pack()
squares = []

sy_list = []
sx_list = []
for i in range(1,101):
    x = randint(20,980)
    y = randint(20,980)
    d = randint(1,10)
    square = c.create_rectangle(x-d,y-d,x+d,y+d,fill='white')
    squares.append(square)
for i in range(1,101):
    sx = randint(-20,20)
    while sx == 0:
        sx = randint(-20,20)
    sx_list.append(sx)
for i in range(1,101):
    sy = randint(-20,20)
    while sy == 0:
        sy = randint(-20,20)
    sy_list.append(sy)
sx = 10
sy = 8
def animate():
    global sx,sy,w,h
    for i in range (len(squares)):
        c.move(squares[i],sx_list[i],sy_list[i])
        x1,y1,x2,y2 = c.coords(squares[i])
        result = c.find_overlapping(x1,y1,x2,y2)
        if x1 < 0 or x2 > w:
            sx_list[i] = -sx_list[i]        
        if y1 < 0 or y2 > h:
            sy_list[i] = -sy_list[i]
        for a in range(len(squares)):
            if squares[a] in result:
                if a < i:
                    
                    
                    c.move(squares[i],10000,10000)
                    sx_list[i] = 0
                    sy_list[i] = 0
                    sx_list[a] += 1
                    sy_list[a] += 1
                if i < a:
                    
                    c.move(squares[a],10000,10000)
                    sx_list[a] = 0
                    sy_list[a] = 0
                    
                    sx_list[i] += 1
                    sy_list[i] += 1
            
    c.after(10,animate)
animate()
