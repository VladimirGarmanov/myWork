a = 456
s = 0
while a > 0:
    if a%10%2 == 0:
        s+=a%10
    a = a//10
print(s)