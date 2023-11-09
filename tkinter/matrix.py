from tkinter import *
root = Tk()
c = Canvas(width=1000,height=1000)
n = int(input('Введите кол-во квадратов:'))
c.pack()
x1 = 100
y1 = 100
x2 = 150
y2 = 150
for a in range(n+1):
    for i in range(n+1):
        c.create_rectangle(x1,y1,x2,y2,fill='blue')
        x1 += 100
        x2 += 100
    y1 += 100
    y2 += 100
    x1 = 100
    x2 = 150
root.mainloop()
