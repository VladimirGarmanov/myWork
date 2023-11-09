ss1 = 10
ss2 = 5
new_number_list = []
amount = 0
for number in range(10,18):
    num = number
    if ss1 == 10 and ss2 < 10:
        while number > 0:
            new_number_list.append(number%ss2)
            number = number//ss2
        new_number_list.reverse()
    for i in range(len(new_number_list)):
        if new_number_list[i] == 2:
            amount+=1

    new_number_list.clear()
print(amount)