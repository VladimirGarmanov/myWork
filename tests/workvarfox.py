for i in range(10):
    age = int(input('age:'))
    if 0<=age<7:
        print('Вам в детский сад')
    if 7<=age<18:
        print('Вам в школу')
    if 18 <= age < 25:
        print('вам в профессиональное заведение')
    if 25<= age < 60:
        print('Вам на работу')
    if 60<=age< 120:
        print("Вам предоставляется выбор")
