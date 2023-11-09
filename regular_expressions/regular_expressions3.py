import re
text = 'Googgle, Gooogggle, Gooooggggle'
a = re.findall(pattern=r'[o]{1,6}|[g]{1,6}', string=text)
print(a)