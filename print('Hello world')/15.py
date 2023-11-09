a = int(input('Введите число:'))
input_numbers = []
for i in range(1024):
    if a // (10 ** i) == 0:
        amount = i
        break

for k in range(amount):
    num = (a % 10 ** (k + 1)) // 10 ** k
    input_numbers.append(num)
input_numbers[1] = 0
input_numbers[3] = 0
output_number = input_numbers[4]*10000 + input_numbers[3]*1000 + input_numbers[2]*100 + input_numbers[1]*10 + input_numbers[0]
print(output_number)
