import re
a = input('String:')
match = re.findall(r'[a-zA-Z.,-]*[@][a-zA-Z.,-]*[.][a-z][a-z]',a)
print(match)
if match[0] == a:
    print('Email is ok')
else:
    print('Invalid email')
