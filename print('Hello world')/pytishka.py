for x in range(1,10001):
    for y in range(1,10001):
        if (x*(y**2)+7) %((x**2)*y+x) == 0:
            print(x,y,x+y)