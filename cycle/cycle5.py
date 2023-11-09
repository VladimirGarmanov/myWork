
input_numbers = []
for a in range(100,1000):
    for i in range(1024):
        if a // (10 ** i) == 0:
            amount = i
            break

    for k in range(amount):
        num = (a % 10 ** (k + 1)) // 10 ** k
        input_numbers.append(num)


    a1 = input_numbers[0]
    a2 = input_numbers[1]
    a3 = input_numbers[2]


    if   (a1**3 + a2**3 + a3**3) == a:
        print(a)
    input_numbers.clear()