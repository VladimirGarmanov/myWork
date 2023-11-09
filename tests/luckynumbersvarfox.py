for a in range(100000,10000000):
    sum1 = 0
    sum2 = 0
    if a != 999999:
        b1 = a
        while b1!= 0:
            sum1 += b1%10
            b1 = b1 // 10
        b2 = a+1
        while b2 != 0:
            sum2 += b2%10
            b2 = b2 // 10
        if sum1 % 13 != 0 and sum2 % 13 != 0:
            print(a,a+1)
