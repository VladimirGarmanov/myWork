from collections import Counter
input_numbers = []
all_numbers = []
for a in range(1000,10000):

    for i in range(1024):
        if a // (10 ** i) == 0:
            amount = i
            break

    for k in range(amount):
        num = (a % 10 ** (k + 1)) // 10 ** k
        input_numbers.append(num)
    double = [k for k, v in Counter(input_numbers).items() if v > 1]


    if double:
        pass

    else:

        all_numbers.append(a)
    double.clear()
    input_numbers.clear()
print(all_numbers)
