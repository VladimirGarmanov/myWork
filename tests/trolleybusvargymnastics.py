for a1 in range(1,10):
    for a2 in range(0,10):
        for a3 in range(0,10):
            for a4 in range(0,10):
                for a5 in range(0,10):
                    for a6 in range(0,10):
                        if a1 + a2 + a3 == a4 + a5 + a6 and ((a1*100000 + a2*10000 + a3*1000 + a4*100 + a5*10 + a6)**0.5)%1 == 0:
                            print(a1*100000 + a2*10000 + a3*1000 + a4*100 + a5*10 + a6)