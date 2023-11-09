a = int(input('Введите число:'))
input_numbers = []
for i in range(1024):
    if a // (10 ** i) == 0:
        amount = i
        break

for k in range(amount):
    num = (a % 10 ** (k + 1)) // 10 ** k
    input_numbers.append(num)

if input_numbers[3] > input_numbers[2] > input_numbers[1] > input_numbers[0]:
    print('yes')
else:
    print('no')