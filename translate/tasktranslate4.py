ss1 = 10
ss2 = 7
new_number_list = []
number = 357
num = number
if ss1 == 10 and ss2 < 10:
    while number > 0:
        new_number_list.append(number%ss2)
        number = number//ss2
    new_number_list.reverse()
    amount = 0
print(len(new_number_list))