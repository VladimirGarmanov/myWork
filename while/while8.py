x = int(input('X:'))
day = 0
y = int(input('Y:'))
p = 10
while x <= y:
    day += 1
    x = x + (x*p)//100
print(day)