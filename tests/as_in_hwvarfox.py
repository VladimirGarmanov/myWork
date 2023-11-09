sum = 0
for i in range(1000,10000):
    b = i
    while b > 0:
        sum += b % 10
        b = b // 10
    if i == sum * 600:
        print(i)
    sum = 0