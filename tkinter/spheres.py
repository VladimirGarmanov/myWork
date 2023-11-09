from tkinter import *
from random import *
window = Tk()
k=0

syl=randint(1,10)
sxl=randint(1,10)
syr=randint(1,10)
sxr=randint(1,10)
syu=randint(1,10)
sxu=randint(1,10)
syd=randint(1,10)
sxd=randint(1,10)

w=600
h=600
c=Canvas(width=w,height=h)
c.pack()
d = 20
circle_left=c.create_oval(0,h/2-d,0+2*d,h/2+d,fill="red")
circle_right = c.create_oval(w-2*d,h/2-d,w,h/2+d,fill='red')
circle_up = c.create_oval(w/2-d,0,w/2+d,2*d,fill='red')
circle_down = c.create_oval(w/2-d,h-2*d,w/2+d,h,fill='red')


def animate():
    global syu,sxl,sxr,syd
    c.move(circle_up,0,syu)
    c.move(circle_left,sxl,0)
    c.move(circle_right,sxr,0)
    c.move(circle_down,0,syd)
    x1l,y1l,x2l,y2l=c.coords(circle_left)
    x1r,y1r,x2r,y2r=c.coords(circle_right)
    x1u,y1u,x2u,y2u=c.coords(circle_up)
    x1d,y1d,x2d,y2d=c.coords(circle_down)
    if x1l<0 or x2l > w:
        sxl = -sxl
    if x1r < 0 or x2r > w:
        sxr = -sxr
    if y1u < 0 or y2u > h:
        syu = -syu
    if y1d < 0 or y2d > h:
        syd = - syd
    c.after(50,animate)
animate()   
mainloop()
