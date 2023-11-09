a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
d = int(input('Введите число:'))
numbers = []
numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers.append(d)
for i in range(len(numbers)):
    if max(numbers) % 2 == 0:
        print(max(numbers))
        break
    if max(numbers) % 2 == 1:
        numbers.remove(max(numbers))
if max(numbers):
    pass
else:
    print('not found')
