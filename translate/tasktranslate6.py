ss1 = 10
ss2 = 4
new_number_list = []
for number in range(1, 26):
    num = number
    if ss1 == 10 and ss2 < 10:
        while number > 0:
            new_number_list.append(number%ss2)
            number = number//ss2
            new_number_list.reverse()
    if len(new_number_list)>1:
        if new_number_list[0] == new_number_list[1] == 1:
            print(num)
    new_number_list.clear()