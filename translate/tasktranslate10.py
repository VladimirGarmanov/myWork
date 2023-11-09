ss1 = 10
ss2 = 6
new_number_list1 = []
new_number_list2 = []
new_number_list = []
ss3 = 5
ss4 = 11


for i in range(1,10000000):
    number = i
    if ss1 == 10 and ss2 < 10:
        while number > 0:
            new_number_list1.append(number%ss2)
            number = number//ss2
    number = i
    if ss1 == 10 and ss3 < 10:
        while number > 0:
            new_number_list2.append(number%ss3)
            number = number//ss3
    if ss4 > 10 and ss1 == 10:
        number = i
        while number > 0:
            if number % ss4 == 10:
                new_number_list.append('A')
            elif number % ss4 == 11:
                new_number_list.append('B')
            elif number % ss4 == 12:
                new_number_list.append('C')
            elif number % ss4 == 13:
                new_number_list.append('D')
            elif number % ss4 == 14:
                new_number_list.append('E')
            elif number % ss4 == 15:
                new_number_list.append('F')
            else:

                new_number_list.append(number % ss4)
            number = number // ss4
    if len(new_number_list1) == 2 and len(new_number_list2) == 3 and new_number_list[0] == 1:
        print(i)
        break



    new_number_list1.clear()
    new_number_list2.clear()
    new_number_list.clear()