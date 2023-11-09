ss1 = 10
ss2 = 9
new_number_list = []

while True:
    number = 100
    num = number
    if ss1 == 10 and ss2 < 10:
        while number > 0:
            new_number_list.append(number%ss2)
            number = number//ss2
        new_number_list.reverse()
    print(new_number_list)


    new_number_list.clear()
    break
