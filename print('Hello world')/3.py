from collections import Counter
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'1))
input_numbers = []
input_numbers.append(a)
input_numbers.append(b)
input_numbers.append(c)

double = [k for k, v in Counter(input_numbers).items() if v > 1]

if double:
    print('yes')
else:
    print('no')