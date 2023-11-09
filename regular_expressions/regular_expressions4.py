import re
text = str(input('N:'))
a = re.findall(pattern=r'^[-|+]?\d+\.\d+$', string=text)
print(a)