numbers = []
for i in range(100,1001):
    if i % 5 == 0 and i % 13==0:
        numbers.append(i)
print(numbers)