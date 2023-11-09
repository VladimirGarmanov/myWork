import re
text = input('String:')
match = re.findall(r'[0-9]',text)
sum = 0
for i in range(len(match)):
    match[i] = int(match[i])
    sum += match[i]
print(sum)