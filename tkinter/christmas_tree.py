from tkinter import *
root = Tk()
c = Canvas(width=1000,height=1000)
c.pack()
n = int(input('Введите кол-во ступеней елки:'))
d = 10
x1 = 100
y1 = 100
x2 = 200
y2 = 5
x3 = 300
y3 = 100
for i in range(n+1):
    c.create_polygon(x1,y1,x2,y2,x3,y3,fill='green')
    y1+=80
    y2+=80
    y3+=80
x1 = 100
y1 = 100
x2 = 200
y2 = 5
x3 = 300
y3 = 100
for a in range(n+1):
    c.create_oval(x1+d,y1+d,x1-d,y1-d,fill='red')
    c.create_oval(x3+d,y1+d,x3-d,y1-d,fill='red')
    c.create_oval(200+d,y1+d,200-d,y1-d,fill='red')

    y1+=80
    y2+=80
    y3+=80
c.create_rectangle(x2-25,y2,x2+25,y1+50,fill='brown')
x1 = 100
y1 = 100
x2 = 200
y2 = 5
x3 = 300
y3 = 100
for i in range(n+1):
    c.create_polygon(x1,y1,x2,y2,x3,y3,fill='green')
    y1+=80
    y2+=80
    y3+=80
x1 = 100
y1 = 100
x2 = 200
y2 = 5
x3 = 300
y3 = 100
for a in range(n+1):
    c.create_oval(x1+d,y1+d,x1-d,y1-d,fill='red')
    c.create_oval(x3+d,y1+d,x3-d,y1-d,fill='red')
    c.create_oval(200+d,y1+d,200-d,y1-d,fill='red')

    y1+=80
    y2+=80
    y3+=80

root.mainloop()
