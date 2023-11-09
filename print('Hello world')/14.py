from collections import Counter
a = int(input('Введите число:'))
input_numbers = []
for i in range(1024):
    if a // (10 ** i) == 0:
        amount = i
        break

for k in range(amount):
    num = (a % 10 ** (k + 1)) // 10 ** k
    input_numbers.append(num)
double = [k for k, v in Counter(input_numbers).items() if v > 1]
print(double)

if double:
    print('yes')
else:
    print('no')
