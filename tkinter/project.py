from tkinter import *
from random import *

root = Tk()
W = 500
H = 500

scale = Scale(root, orient=HORIZONTAL, length=200, to=50, resolution=1)
scale.pack(side=LEFT)

c = Canvas(root, width=W, height=H)
c.pack()

r = 1
a = 'white'
b = 'white'
c = 'white'
d = 'white'
e = 'white'
f = 'white'
g = 'white'


def move_mouse(event):
    global r, a
    r = scale.get()
    x, y = event.x, event.y  # even = метод считывает координаты мышки
    c.create_oval(x - r, y - r, x + r, y + r, fill=a, outline='')  # уз чёрной обводки


c.bind('<Motion>', move_mouse)  # bind = метод привязывающий всё, Motion = реогирует на движения мышки


def color_paint1():
    global a
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    a = rainbow[0]


def color_paint2():
    global a
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    a = rainbow[1]


def color_paint3():
    global a
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    a = rainbow[2]


def color_paint4():
    global a
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    a = rainbow[3]


def color_paint5():
    global a
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    a = rainbow[4]


def color_paint6():
    global a
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    a = rainbow[5]


def color_paint7():
    global a
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    a = rainbow[6]


button1 = Button(root, width=5, height=5, bg='Red', fg='red', font='arial 14', command=color_paint1)
button2 = Button(root, width=5, height=5, bg='Orange', fg='red', font='arial 14', command=color_paint2)
button3 = Button(root, width=5, height=5, bg='Yellow', fg='red', font='arial 14', command=color_paint3)
button4 = Button(root, width=5, height=5, bg='Green', fg='red', font='arial 14', command=color_paint4)
button5 = Button(root, width=5, height=5, bg='Blue', fg='red', font='arial 14', command=color_paint5)
button6 = Button(root, width=5, height=5, bg='Indigo', fg='red', font='arial 14', command=color_paint6)
button7 = Button(root, width=5, height=5, bg='Violet', fg='red', font='arial 14', command=color_paint7)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)

root.mainloop()