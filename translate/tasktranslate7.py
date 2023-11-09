from random import *
ss2 = 10

ss1 = 8
new_number_list = []
new_number1 = 0
new_number2 = 0
for i in range(1,1000):
    if ss2 == 10 and ss1 < 10:
        number = i
        number2 = number*100
        while number > 0:
            new_number_list.append(number%10)
            number = number//10
        for a in range(len(new_number_list)):
            new_number1 += new_number_list[a]*(ss1**a)
    new_number_list.clear()
    if ss2 == 10 and ss1 < 10:
        while number2 > 0:
            new_number_list.append(number2%10)
            number2 = number2//10
        for a in range(len(new_number_list)):
            new_number2 += new_number_list[a]*(ss1**a)
    new_number_list.clear()
    print(new_number2/new_number1)
