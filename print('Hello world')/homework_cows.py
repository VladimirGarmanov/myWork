from random import randint
cow = 0
bull = 0
num_try = 0
amout_g = 0
random_numbers = []
guess = randint(100,999)
print(guess)
for j in range(1024):
    if guess//(10**j) == 0:
        amount_g = j
        break
for g in range(amount_g):
    num_g = (guess%10**(g+1)) // 10**g
    random_numbers.append(num_g)
while True:

    num_try+=1
    print(f'Quantity of cows:{cow}\nQuantity of bulls:{bull}')
    cow = 0
    bull = 0
    a = int(input('Input the number:'))
    amount = 0
    input_numbers = []

    for i in range(1024):
        if a//(10**i) == 0:
            amount = i
            break

    for k in range(amount):
        num = (a%10**(k+1)) // 10**k
        input_numbers.append(num)
    if guess == a:
        print(f'You won, it took you {num_try} tries')
        break
    for p in range(3):
        if random_numbers[p] == input_numbers[p]:
            bull+=1
        if random_numbers[p] in input_numbers and random_numbers[p] != input_numbers[p]:
            cow+=1
