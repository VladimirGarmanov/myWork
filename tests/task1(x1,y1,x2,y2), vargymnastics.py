x1 = int(input('x1:'))
y1 = int(input('y1:'))
x2 = int(input('x2:'))
y2 = int(input('y2:'))
if x1 < x2 :
    print('Точка 2 правее точки 1')
if x2 < x1:
    print('Точка 1 правее точки 2')
if y1 < y2:
    print('Точка 2 выше точки 1')
if y2 < y1:
    print('Точка 1 выше точки 2 ')