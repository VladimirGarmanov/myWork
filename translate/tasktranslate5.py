ss1 = 10
ss2 = 2
new_number_list = []
number = 16
amount = 0
amount_list = []
for i in range(2,16):
    num = number
    if ss1 == 10 and ss2 < 10:
        while number > 0:
            new_number_list.append(number%ss2)
            number = number//ss2
    number = num + 16
    for a in range(len(new_number_list)-1):
        if new_number_list[a] == 0:
            amount += 1
        if new_number_list[a] == 1:
            amount_list.append(amount)
            break

    new_number_list.clear()
    amount = 0
print(min(amount_list))
