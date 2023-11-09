a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
output = []
sum = 0
if a % 5 == 0:
    output.append(a)
if b % 5 == 0:
    output.append(b)
if c % 5 == 0:
    output.append(c)

for k in range(len(output)):
    sum += output[k]
if sum == 0:
    print('error')
if sum != 0 :

    print(sum)
