all_numbers = []
numbers = []
for i in range(1000,10000):
    if (i%10)//1 == 5 or (i%100)//10 == 5 or (i%1000)//100 == 5 or (i%10000)//1000 == 5 or (i%10)//1 == 6 or (i%100)//10 == 6 or (i%1000)//100 == 6 or (i%10000)//1000 == 6:
        pass
    else:
        all_numbers.append(i)
print(all_numbers)