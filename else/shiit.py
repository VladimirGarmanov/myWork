numbers = []
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    x = a*10000 + b*1000 + c*100 + d*10 + e
                    print(x)
                    numbers.append(x)



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