input_numbers = []
for a in range(1000, 10000):
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
    a4 = input_numbers[3]

    if (a1+a2+a3+a4)*600 == a:
        print(a)
    input_numbers.clear()