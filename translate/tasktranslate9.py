ss1 = 10
ss2 = 3
new_number_list1 = []
new_number_list2 = []
ss3 = 5


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
    if new_number_list1[0] == 0 and new_number_list2[0] == 0:
        print(i)
        break



    new_number_list1.clear()
    new_number_list2.clear()