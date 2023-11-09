for a in range(1,100):
    for b in range(1,100):
        if ((a**2+b**2)**0.5)% 1 == 0:
            print(a,b,int((a**2+b**2)**0.5))
