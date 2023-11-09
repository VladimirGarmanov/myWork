numbers = []
for i in range(1000,10001):
    numbers.append(i)
for j in range(len(numbers)):
    for k in range(2,numbers[j]):
        if numbers[j]%k == 0:
            numbers[j] = 0
right_numbers = []
for l in range(len(numbers)):
    if numbers[l] != 0:
        right_numbers.append(numbers[l])

print(right_numbers)
