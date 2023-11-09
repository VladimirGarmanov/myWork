import re
str1 = input('String1:')
match1 = re.findall(r'[a-zA-Z]', str1)
notlone1 = []
str2 = input('String2:')
match2 = re.findall(r'[a-zA-Z]', str2)
notlone2 = []
for i in range(len(str1)):
    for j in range(len(str1)):
        if str1[i] == str1[j] and i!= j:
            notlone1.append(str1[i])
for k in range(len(notlone1)):
    if notlone1[k] in match1:
        match1.remove(notlone1[k])
for h in range(len(str2)):
    for g in range(len(str2)):
        if str2[h] == str2[g] and h != g:
            notlone2.append(str2[h])
for q in range(len(notlone2)):
    if notlone2[q] in match2:
        match2.remove(notlone2[q])
print(list(set(match1) & set(match2)))