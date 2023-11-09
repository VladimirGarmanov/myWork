a = int(input('Введите число:'))
arabic_numbers = []
romanian_units = ['I', 'II', 'III', 'IV', 'VI', 'VII', 'VIII', 'IX', 'X']
romanian_dozens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
romanian_hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
romanian_thousands = ['M', 'MM', 'MMM']
for i in range(1024):
    if a // (10 ** i) == 0:
        amount = i
        break

for k in range(amount):
    num = (a % 10 ** (k + 1)) // 10 ** k
    arabic_numbers.append(num)
print(f'{romanian_thousands[arabic_numbers[3]-1]}{romanian_hundreds[arabic_numbers[2]-1]}{romanian_dozens[arabic_numbers[1]-1]}{romanian_units[arabic_numbers[0]-1]}')

