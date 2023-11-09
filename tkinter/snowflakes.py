from tkinter import *
from random import *
import math
win = Tk()
w = 800
h = 800
c = Canvas(width = w, height = h)
c.pack()
snowflakes = []
d = 10
list_coords = []
sx_list = []
r = 10

n = 15
list_coords = []
dx = 50
for i in range(1,1000):
    
    dy = randint(600,1500)
    dx = randint(10,800)

    for k in range(n):
        if n % 2 == 0:
            k1 = (k + n / 2 - 1) % n
        else:
            k1 = (k + (n - 1) / 2) % n

        p1 = (dx + r * math.cos(2 * 3.14 * k / n), 0-dy + r * math.sin(2 * 3.14 * k / n))
        p2 = (dx + r * math.cos(2 * 3.14 * k1 / n), 0-dy + r * math.sin(2 * 3.14 * k1 / n))
        list_coords.append(p1)
        list_coords.append(p2)
    snowflake = c.create_polygon(list_coords[0], list_coords[1],list_coords[2],list_coords[3],list_coords[4],list_coords[5],list_coords[6],list_coords[7],list_coords[8],list_coords[9],list_coords[10],list_coords[11],list_coords[12],list_coords[13],list_coords[14],list_coords[15],list_coords[16],list_coords[17],list_coords[18],list_coords[19],list_coords[20],list_coords[21],list_coords[22],list_coords[23],list_coords[24],list_coords[25],list_coords[26],list_coords[27],list_coords[28],list_coords[29], fill = 'white')
    list_coords.clear()
    snowflakes.append(snowflake)
for i in range(1,1000):
    sx = randint(5,15)
    sx_list.append(sx)
    
sx = 5
def animate():
    global sx,sy,w,h
    for i in range (len(snowflakes)):
        c.move(snowflakes[i],0,sx_list[i])
        

        
        if c.coords(snowflakes[i])[1] > 800:
            c.move(snowflakes[i],0,-800)
        sx = 5
        
        
        
    c.after(10,animate)
a1=c.create_oval(35,320,65,350,fill='white')
a2=c.create_oval(25,350,75,400,fill='white')
a3=c.create_oval(0,400,100,500,fill='white')
c1=c.create_rectangle(35,330,65,300,fill='grey')
c2=c.create_line(40,335,45,335,fill='red')
c3=c.create_line(55,335,60,335,fill='red')
n = 3
d = 10
x1 = 600
y1 = 100
x2 = 700
y2 = 5
x3 = 800
y3 = 100
for i in range(n+1):
    c.create_polygon(x1,y1,x2,y2,x3,y3,fill='green')
    y1+=80
    y2+=80
    y3+=80
x1 = 600
y1 = 100
x2 = 700
y2 = 5
x3 = 800
y3 = 100
for a in range(n+1):
    c.create_oval(x1+d,y1+d,x1-d,y1-d,fill='red')
    c.create_oval(x3+d,y1+d,x3-d,y1-d,fill='red')
    c.create_oval(700+d,y1+d,700-d,y1-d,fill='red')

    y1+=80
    y2+=80
    y3+=80
c.create_rectangle(x2-25,y2,x2+25,y1+50,fill='brown')
x1 = 600
y1 = 100
x2 = 700
y2 = 5
x3 = 800
y3 = 100
for i in range(n+1):
    c.create_polygon(x1,y1,x2,y2,x3,y3,fill='green')
    y1+=80
    y2+=80
    y3+=80
x1 = 600
y1 = 100
x2 = 700
y2 = 5
x3 = 800
y3 = 100
for a in range(n+1):
    c.create_oval(x1+d,y1+d,x1-d,y1-d,fill='red')
    c.create_oval(x3+d,y1+d,x3-d,y1-d,fill='red')
    c.create_oval(700+d,y1+d,700-d,y1-d,fill='red')

    y1+=80
    y2+=80
    y3+=80


animate()
win.mainloop()
