for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if b >-1*a - c and b**2 <= 4*(-1*a)*(-1*c):
                print(a,b,c)