

import tkinter
import math
from random import randint
from time import time
win = tkinter.Tk()
c = tkinter.Canvas(win , bg='black', height=600, width=600)
c.pack()

r = 30

n = 15
list_coords = []
dx = 50
for i in range(1,8):
    
    dy = randint(30,100)

    for k in range(n):
        if n % 2 == 0:
            k1 = (k + n / 2 - 1) % n
        else:
            k1 = (k + (n - 1) / 2) % n

        p1 = (dx + r * math.cos(2 * 3.14 * k / n), dy + r * math.sin(2 * 3.14 * k / n))
        p2 = (dx + r * math.cos(2 * 3.14 * k1 / n), dy + r * math.sin(2 * 3.14 * k1 / n))
        list_coords.append(p1)
        list_coords.append(p2)
    c.create_polygon(list_coords[0], list_coords[1],list_coords[2],list_coords[3],list_coords[4],list_coords[5],list_coords[6],list_coords[7],list_coords[8],list_coords[9],list_coords[10],list_coords[11],list_coords[12],list_coords[13],list_coords[14],list_coords[15],list_coords[16],list_coords[17],list_coords[18],list_coords[19],list_coords[20],list_coords[21],list_coords[22],list_coords[23],list_coords[24],list_coords[25],list_coords[26],list_coords[27],list_coords[28],list_coords[29], fill = 'white')
    list_coords.clear()
    dx += 80
x = 100
c.create_rectangle(50+x,600,140+x,400,fill='green')
c.create_rectangle(140+x,600,230+x,500,fill='green')
c.create_rectangle(230+x,600,320+x,400,fill='green')
y1 = 590
y2 = 570
for i in range(6):
    light = randint(0,1)
    if light == 1:
        color = 'yellow'
    if light == 0:
        color = 'black'
    
    c.create_rectangle(50+x+10,y1,50+x+30,y2,fill=color)
    light = randint(0,1)
    if light == 1:
        color = 'yellow'
    if light == 0:
        color = 'black'
    c.create_rectangle(50+x+60,y1,50+x+80,y2,fill=color)
    y1-=30
    y2-=30
x = 190
y1 = 590
y2 = 570
for i in range(3):
    light = randint(0,1)
    if light == 1:
        color = 'yellow'
    if light == 0:
        color = 'black'
    
    c.create_rectangle(50+x+10,y1,50+x+30,y2,fill=color)
    light = randint(0,1)
    if light == 1:
        color = 'yellow'
    if light == 0:
        color = 'black'
    c.create_rectangle(50+x+60,y1,50+x+80,y2,fill=color)
    y1-=30
    y2-=30
y1 = 590
y2 = 570
x = 280

for i in range(6):
    light = randint(0,1)
    if light == 1:
        color = 'yellow'
    if light == 0:
        color = 'black'
    c.create_rectangle(50+x+10,y1,50+x+30,y2,fill=color)
    light = randint(0,1)
    if light == 1:
        color = 'yellow'
    if light == 0:
        color = 'black'
    c.create_rectangle(50+x+60,y1,50+x+80,y2,fill=color)
    y1-=30
    y2-=30
x = 100
lift1 = c.create_rectangle(((50+140+x+x)/2)-10,590,((50+140+x+x)/2)+10,560,fill='brown')
x = 190
lift2 = c.create_rectangle(((50+140+x+x)/2)-10,590,((50+140+x+x)/2)+10,560,fill='brown')
x = 280
lift3 = c.create_rectangle(((50+140+x+x)/2)-10,590,((50+140+x+x)/2)+10,560,fill='brown')
y11 = 560
sx1 = -5
sx2 = -5
sx3 = -5
def move_lifts():
    global lift1,y11,sx1,lift2,lift3,sx2,sx3
    if sx1 > 0:
        vector1 = False
    if sx1 < 0:
        vector1 = True

    
    c.move(lift1,0,sx1)
    x1,y1,x2,y2 = c.coords(lift1)
    if y2 == 560 or y2 == 530 or y2 == 500 or y2 == 470 or y2 == 440 or y2 == 590 :
        a = time()
        while time() - a < 1:
            sx1 = 0
        if vector1 == True:
            sx1 = -5
        if vector1 == False:
            sx1 = 5
    if y2 < 430:
        sx1 = -sx1
        print('gbjfhbkgch')
    
    if y2 > 590:
        sx1 = -sx1

        
    if sx2 > 0:
        vector2 = False
    if sx2 < 0:
        vector2 = True
    
    
    c.move(lift2,0,sx2)
    x12,y12,x22,y22 = c.coords(lift2)
    if y22 == 560 or y22 == 530 or y22 == 590 :
        a2 = time()
        while time() - a2 < 1:
            sx2 = 0
        if vector2 == True:
            sx2 = -5
        if vector2 == False:
            sx2 = 5
    if y22 < 520:
        sx2 = -sx2
        print('gbjfhbkgch')
    
    if y22 > 591:
        sx2 = -sx2
    if sx3 > 0:
        vector3 = False
    else:
        vector3 = True

    
    c.move(lift3,0,sx3)
    x3,y13,x23,y23 = c.coords(lift3)
    if y23 == 560 or y23 == 530 or y23 == 500 or y23 == 470 or y23 == 440 or y23 == 590 :
        a3 = time()
        while time() - a3 < 1:
            sx3 = 0
        if vector3 == True:
            sx3 = -5
        if vector3 == False:
            sx3 = 5
    if y23 < 430:
        sx3 = -sx3
        print('gbjfhbkgch')
    
    if y23 > 590:
        sx3 = -sx3
    c.after(100,move_lifts)
    
move_lifts()
win.mainloop()
