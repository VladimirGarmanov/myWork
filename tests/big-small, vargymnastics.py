a = int(input('a:'))
numbers = []
while a != 0:
    numbers.append(a % 10)
    a = a // 10
numbers.sort()
print(numbers)

