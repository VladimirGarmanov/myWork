a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d = int(input('d:'))
number = []
number.append(a)
number.append(b)
number.append(c)
number.append(d)
amount = 0
for i in number:
    for j in number:
        if i == j:
            amount += 1
if amount == 8:
    print(a,b,c,d)
