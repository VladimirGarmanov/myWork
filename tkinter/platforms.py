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
for i in range(1,4):
    x = randint(25,w-25)
    y = randint(0,100)
    snowflake = c.create_rectangle(x-25,y+5,x+25,y-5,fill='brown')
    
    
    snowflakes.append(snowflake)
for i in range(1,4):
    sx = randint(5,15)
    sx_list.append(sx)
    
sx = 5
minion = c.create_oval(-50,h/2-25,0,h/2+25,fill='yellow')
sy = 0



def animate():
    global sx,sy,w,h
    c.move(minion,sx,sy)
    x1,y1,x2,y2 = c.coords(minion)
    result = c.find_overlapping(x1,y1,x2,y2)
    if x1 > w:
        c.move(minion,-w,0)
    for i in range (len(snowflakes)):
        c.move(snowflakes[i],0,5)
        if snowflakes[i] in result:
            sx = 0
            sy = 5
            
        

        
        if c.coords(snowflakes[i])[1] > 800:
            c.move(snowflakes[i],0,-800)
    c.after(10,animate)
animate()
win.mainloop()
