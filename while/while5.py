n = int(input('n:'))
m = int(input('m:'))
i = 0
h = -1
sum = 0
input_numbers = []
while h < n:
    h+=1
    while i < 1024:
        if h // (10 ** i) == 0:
            amount = i
            break
        i += 1

    for k in range(amount):
        num = (h % (10 ** (k + 1))) // 10 ** k
        input_numbers.append(num)
    for l in range(len(input_numbers)):
        sum += input_numbers[l]
    if sum**2 == m:
        print(h)
    input_numbers.clear()
    amount = 0
    sum = 0



