S = int(input('S:'))
for a in range(1,2*S+1):
    for b in range(1,2*S+1):
        if a*b*0.5 <= S and ((a**2 + b **2)**0.5) % 1 == 0:
            print(a,b,int(((a**2+b**2)**0.5)))