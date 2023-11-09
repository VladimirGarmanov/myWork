day1 = int(input('Введите день:'))
month1 = int(input('Введите месяц:'))
year1 = int(input("Введите год:"))
day2 = int(input('Введите день:'))
month2 = int(input('Введите месяц:'))
year2 = int(input("Введите год:"))
if year1 < year2:
    print('yes')


if year1 == year2:

    if  month1 < month2:
        print('yes')

    if month1 == month2:
        if day1 < day2:
            print('yes')

        else:
            print('no')
