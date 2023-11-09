import re
from random import *
our_password = []
symbols = randint(9,15)
password = input('Passowrd:')
sp_chr = [',','.','/',' ','[', ']', '{','}','@',]
num = ['0','1','2','3','4','5','6','7','8','9']
words = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','K','Z','X','C','V','B','N','M']
match = re.findall(r'[a-z|A-Z|.|,|/| 0-9|{|}|@|<|>]', password)
for i in range(symbols):
    type_symbol = randint(1,3)
    if type_symbol == 1:
        which_sym = randint(0,len(sp_chr)-1)
        our_password.append(sp_chr[which_sym])
    if type_symbol == 2:
        which_sym = randint(0, len(num) - 1)
        our_password.append(num[which_sym])
    if type_symbol == 3:
        which_sym = randint(0, len(words) - 1)
        our_password.append(words[which_sym])
print(match)
password_string = ''.join(our_password)
if len(list(set(sp_chr)& set(match)))>0 and len(list(set(num)& set(match)))>0 and  len(list(set(words)& set(match)))>0 and len(password)>8:
    print('Password is normal')
else:
    print('Try a new one')
    print(f'You can use safe password: {password_string}')