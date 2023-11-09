n = int(input('N:'))
i = 2
simple_digit = []
min = 1
while i * i <= n:
    while n % i == 0:
        if i > min:
            min = i
        n = n / i
    i = i + 1
if n > 1:
    if n > min:
        min = int(n)
print(min)