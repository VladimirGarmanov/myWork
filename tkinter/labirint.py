from tkinter import *
win = Tk()
w = 1000
h = 800
c = Canvas(width = w, height = h)
c.pack()
circle = c.create_oval(10,10,60,60,fill = 'red')
rec1 = c.create_rectangle(200,200,300,h,fill = 'blue')
rec2 = c.create_rectangle(w/2-50,0,w/2+50,h-200, fill = 'blue')
rec3 = c.create_rectangle(750,200,850,h,fill = 'blue')
sx = 5
sy = 0

def animate():
    global sx,sy
    c.move(circle,sx,sy)
    x1,y1,x2,y2 = c.coords(circle)
    if x2 == 400:
        sx = 0
        sy = 5
    if y1 == h-100:
        sx = 5
        sy = 0
    if x2 == 650:
        sx = 0
        sy = -5
    if y2 <= 50:
        sx = 5
        sy = 0
    if x2 >= 900:
        sx = 0
        sy = 10
    c.after(10,animate)
animate()
