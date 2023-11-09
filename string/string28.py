import re
text = input()
a = re.findall(pattern=r'[ ]{1,10000}', string=text)
print(len(max(a)))