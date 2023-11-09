
ss1 = int(input('Введите первую систему счисления:'))
ss2 = int(input('Введите вторую систмеу счисления:'))
new_number_list = []
new_number = 0
if ss1 == 10 and ss2 < 10:
    number = int(input('Number'))
    while number > 0:
        new_number_list.append(number%ss2)
        number = number//ss2
    new_number_list.reverse()
    print(new_number_list)
if ss2 == 10 and ss1 < 10:
    number = int(input('Введите число:'))
    while number > 0:
        new_number_list.append(number%10)
        number = number//10
    for a in range(len(new_number_list)):
        new_number += new_number_list[a]*(ss1**a)
    print(new_number)
if ss1 < 10 and ss2 < 10:
    number = int(input('Введите число:'))
    while number > 0:
        new_number_list.append(number%10)
        number = number//10
    for a in range(len(new_number_list)):
        new_number += new_number_list[a]*(ss1**a)
    new_number_list.clear()
    number = new_number
    while number > 0:
        new_number_list.append(number%ss2)
        number = number//ss2
    new_number_list.reverse()
    print(new_number_list)
if ss1 > 10 and ss2 == 10:
    number = str(input('Введите число:'))
    if len(number) > 0:
        number[::-1]
    for i in range(len(number)):
        if str(number)[i] == 'A':
            new_number += 10*(ss1**i)
        elif str(number)[i] == 'B':
            new_number += 10 * (ss1 ** i)
        elif str(number)[i] == 'C':
            new_number += 10 * (ss1 ** i)
        elif str(number)[i] == 'D':
            new_number += 10 * (ss1 ** i)
        elif str(number)[i] == 'E':
            new_number += 10 * (ss1 ** i)
        elif str(number)[i] == 'F':
            new_number += 10 * (ss1 ** i)
        elif str(number)[i] == 'G':
            new_number += 10 * (ss1 ** i)
        else:


            new_number += int(str(number)[i])*(ss1**a)
        print(new_number)
if ss2 > 10 and ss1 == 10:
    number = int(input('Введите число:'))
    while number > 0:
        if number%ss2 == 10:
            new_number_list.append('A')
        elif number%ss2 == 11:
            new_number_list.append('B')
        elif number%ss2 == 12:
            new_number_list.append('C')
        elif number%ss2 == 13:
            new_number_list.append('D')
        elif number%ss2 == 14:
            new_number_list.append('E')
        elif number%ss2 == 15:
            new_number_list.append('F')
        else:

            new_number_list.append(number%ss2)
        number = number//ss2
    new_number_list.reverse()
    print(new_number_list)
