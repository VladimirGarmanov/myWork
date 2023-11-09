a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if a < 5 and b < 5 and c >5:
    print('yes')
elif a < 5 and c < 5 and b >5:
    print('yes')
elif b < 5 and c < 5 and a >5:
    print('yes')
else:
    print('no')