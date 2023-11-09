ss1 = 10
ss2 = 5
new_number_list = []
for number in range(1, 31):
    num = number
    if ss1 == 10 and ss2 < 10:
        while number > 0:
            new_number_list.append(number%ss2)
            number = number//ss2
        new_number_list.reverse()
    amount = 0
    if new_number_list[0] == 3:
        print(num)
    new_number_list.clear()