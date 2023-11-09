n = int(input('N:'))
i = 2
simple_digit = []
while i * i <= n:
    while n % i == 0:
        simple_digit.append(i)
        n = n / i
    i = i + 1
if n > 1:
    simple_digit.append(int(n))
print(max(simple_digit))