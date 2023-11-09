a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
numbers = []
numbers.append(a+b)
numbers.append(b+c)
numbers.append(c+a)
if max(numbers)  == numbers[0]:
    print(a)
    print(b)

elif max(numbers) == numbers[1]:
    print(b)
    print(c)

elif max(numbers) == number[2]:
    print(c)
    print(a)
