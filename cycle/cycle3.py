num = []
for i in range(1016,7938):
    if i %3 == 0 and i%7 != 0 and i%17 != 0 and  i%19 != 0 and i%27 != 0 :
        num.append(i)
print(max(num))
print(len(num))
