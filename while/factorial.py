
digit = 1
i = 1
for a in range(1,10000):
    while i <= a:
        digit *=i
        i+=1
    if (digit + 1) % (a + 1) == 0:
        print(a)

