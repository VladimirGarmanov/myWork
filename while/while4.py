a = int(input('Введите число:'))
input_numbers = []
i = 0
while i < 1024:
    if a // (10 ** i) == 0:
        amount = i
        break
    i+=1

for k in range(amount):
    num = (a % 10 ** (k + 1)) // 10 ** k
    input_numbers.append(num)
if 2 in input_numbers:
    print('yes')
else:
    print('no')